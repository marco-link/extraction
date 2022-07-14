#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script using :mod:`Root.RDataFrame` to produce histograms.
View arguments with ``python python/fill_histos.py -h``.
"""

import datetime
import numpy
import argparse

from ROOT import TH1, ROOT, TFile

from helpers import getSystsplit, getDatasetInfo, get_event_weigths
from config.general import general, getGridpaths, histopath, lumi
from config.data import data
from config.datasets import datasets
from config.regions import regions
from config.histograms import histograms
from config.systematics import systematics

datasets.update(data)

TH1.SetDefaultSumw2(True)
TH1.StatOverflows(True)

RDF = ROOT.RDataFrame
TM1 = ROOT.RDF.TH1DModel



def fillhistos(year, region, dataset, systematic, number, cuts):
    """
    fill histograms

    :param year: year
    :param region: region name
    :param dataset: dataset name
    :param systematic: systematic name
    :param number: file number
    :param cuts: cuts to apply
    """
    starttime = datetime.datetime.now()
    print(f'\nSTARTING AT {str(starttime)}')

    print(f'Year: {year}')
    print(f'dataset: {dataset}')
    print(f'Region: {region}')
    print(f'Systematic: {systematic}')

    gridpaths = getGridpaths(isMC=datasets[dataset]['MC'], year=year, filename=datasets[dataset]['FileName'])

    inFileName = gridpaths[number]
    outFileName = histopath(year=year, region=region, dataset=dataset, systematic=systematic, number=number)

    # get original dataset size from number of entries (before cuts/filters) and preskim efficiency
    datasetInfo = getDatasetInfo(gridpaths, MC=datasets[dataset]['MC'])

    weights = get_event_weigths(year, dataset, systematic, datasetInfo)
    print('EventWeights: {}'.format(weights))

    print('\nOPENING INPUT FILE AND CREATING DATAFRAME')
    dataframe = RDF(general['Tree'], inFileName)


    for cut in cuts:
        if cut != 'none':
            print(f'Applying additional cut: {cut}')
            dataframe = dataframe.Filter(cut, cut)

    if 'Filter' in regions[region].keys():
        mask = regions[region]['Filter']
        if datasets[dataset]['MC']:
            mask = mask.replace('nominal', systematic)
        print(f'Applying region filter: {mask}')
        dataframe = dataframe.Filter(mask, region)


    dataframe = dataframe.Define('w', weights)


    print('\nLOOPING OVER HISTOGRAMS')
    histos = {}

    for histname in histograms.keys():
        systematic, direction = getSystsplit(systematic)
        branchname = histograms[histname]['Branch']

        if datasets[dataset]['MC']:
            branchname = histograms[histname]['Branch'].replace('nominal', systematic)

            if 'Branch' in systematics[systematic].keys():
                branchname = branchname.replace('nominal', systematics[systematic]['Branch'][direction])


        print(f'Reading from branch "{branchname}"...')


        if 'datasets' in histograms[histname].keys() and dataset not in histograms[histname]['datasets']:
            print(f'Skipping histogram generation for "{histname}" (histogram not defined for this dataset)')
            continue

        if 'Expression' in histograms[histname].keys():
            expression = histograms[histname]['Expression']
            if datasets[dataset]['MC']:
                expression = expression.replace('nominal', systematic)

            print(f'\nAdding temporary branch "{histname}" from Expression: {expression}')
            dataframe = dataframe.Define(branchname, expression)

        if branchname in dataframe.GetColumnNames():
            histogram = {}
            if 'Histogram' in histograms[histname].keys():
                histogram = histograms[histname]['Histogram']

            print(f'Adding histogram for {histname} with weights {weights}')
            if 'varbins' in histogram.keys():
                histos[histname] = dataframe.Histo1D(TM1(histname,
                                                     histname,
                                                     histogram['nbins'],
                                                     numpy.array(histogram['varbins'])),
                                                     branchname, 'w')
            else:
                histos[histname] = dataframe.Histo1D(TM1(histname,
                                                     histname,
                                                     histogram['nbins'],
                                                     histogram['xmin'],
                                                     histogram['xmax']),
                                                     branchname, 'w')


            # do not ask for the histogram entries or anything that requires processing
            # the ntuple at this step!!!
        else:
            print(f'\n\n\tERROR: Branch "{branchname}" defined in config/histogram.py not found!\n')


    print('\n\n==============Config Summary===============')
    print('Systematic: {}'.format(systematic))
    print('Output: {}'.format(outFileName))
    print('Region: {}'.format(region))
    print('===========================================\n\n')

    print('\nFILLING HISTOGRAMS')

    scale = 1.
    if datasets[dataset]['MC']:
        scale = 1000 * datasets[dataset]['XS'] * datasets[dataset][year]['KFactor'] * lumi[year]

    #this will trigger the event loop

    for histname in histograms.keys():
        print(histname)
        histos[histname].Scale(scale)
        print(f'selected {histos[histname].GetEntries()} events out of {datasetInfo["genEventCount"]} (genEventCount)')
        print(f"scaled with {scale:.3g} = {1000*datasets[dataset]['XS']:.1f}(XS in fb) \
* {datasets[dataset][year]['KFactor']}(K-factor) * {lumi[year]}(lumi in 1/fb)")

    print('\nREPORT')
    report = dataframe.Report()

    outFile = TFile(outFileName, 'UPDATE')
    histoDir = outFile.Get(general['Histodir'])
    if not histoDir:
        histoDir = outFile.mkdir(general['Histodir'])
    histoDir.cd()
    for histogram in sorted(histos.keys()):
        histoDir.Append(histos[histogram].GetPtr(), True)
    histoDir.Write('', TFile.kOverwrite)
    outFile.Close()

    print('OUTPUT WRITTEN TO {}'.format(outFileName))

    print('\n\n==============Selection Efficiencies===============')
    report.Print()

    endtime = datetime.datetime.now()
    print('\nFINISHING AT {}, TAKING IN TOTAL {}'.format(str(endtime), endtime - starttime))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--year', type=str, required=True,
                        help='year to process')

    parser.add_argument('--region', type=str, required=True,
                        help='region to process')

    parser.add_argument('--dataset', type=str, required=True,
                        help='dataset to process')

    parser.add_argument('--systematic', type=str, default='nominal',
                        help='systematic to process')

    parser.add_argument('--number', type=int, required=True,
                        help='number of input file')

    parser.add_argument('--cuts', action='store', default=[], nargs='+',
                        help='cuts to apply')


    args = parser.parse_args()

    print(f'Converting {args.dataset}')

    fillhistos(year=args.year,
               region=args.region,
               dataset=args.dataset,
               systematic=args.systematic,
               number=args.number,
               cuts=args.cuts)
