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

from helpers import getSystsplit, get_event_weigths
from config.general import general, samplepath, histopath, lumi, getDatasetSize
from config.samples import samples
from config.regions import regions
from config.histograms import histograms
from config.systematics import systematics


TH1.SetDefaultSumw2(True)
TH1.StatOverflows(True)

# enable multi-threading
ROOT.EnableImplicitMT()
RDF = ROOT.RDataFrame
TM1 = ROOT.RDF.TH1DModel


def fillhistos(year, region, sample, systematic, cuts):
    """
    fill histograms

    :param year: year
    :param region: region name
    :param sample: sample name
    :param systematic: systematic name
    :param cuts: cuts to apply
    """
    starttime = datetime.datetime.now()
    print(f'\nSTARTING AT {str(starttime)}')

    print(f'Year: {year}')
    print(f'Sample: {sample}')
    print(f'Region: {region}')
    print(f'Systematic: {systematic}')

    weights = get_event_weigths(year, sample, systematic)
    print('EventWeights: {}'.format(weights))

    inFileName = samplepath(isMC=samples[sample]['MC'], year=year, filename=samples[sample]['FileName'])
    outFileName = histopath(isMC=samples[sample]['MC'], year=year, filename=sample, region=region, systematic=systematic)

    # get original dataset size from number of entries (before cuts/filters) and preskim efficiency
    dataset_size = getDatasetSize(inFileName)

    print('\nOPENING INPUT FILE AND CREATING DATAFRAME')
    df_in = RDF(general['Tree'], inFileName)
    df_out = df_in



    for cut in cuts:
        if cut != 'none':
            print(f'Applying additional cut: {cut}')
            df_out = df_out.Filter(cut, cut)

    if 'Filter' in regions[region].keys():
        print(f'Applying region filter: {regions[region]["Filter"]}')
        df_out = df_out.Filter(regions[region]['Filter'], region)


    df_out = df_out.Define('w', weights)


    print('\nLOOPING OVER HISTOGRAMS')
    histos = {}
    for histname in histograms.keys():
        systematic, direction = getSystsplit(systematic)
        branchname = histograms[histname]['Branch']

        if 'Branch' in systematics[systematic].keys():
            branchname = branchname.replace('nominal', systematics[systematic]['Branch'][direction])

        print(f'Reading from branch "{branchname}"...')


        if 'Samples' in histograms[histname].keys() and sample not in histograms[histname]['Samples']:
            print(f'Skipping histogram generation for "{histname}" (histogram not defined for this sample)')
            continue

        if 'Expression' in histograms[histname].keys():
            print(f'\nAdding temporary branch "{histname}" from Expression: {histograms[histname]["Expression"]}')
            df_out = df_out.Define(branchname, histograms[histname]['Expression'])

        if branchname in df_out.GetColumnNames():
            histogram = {}
            if 'Histogram' in histograms[histname].keys():
                histogram = histograms[histname]['Histogram']

            print(f'Adding histogram for {histname} with weights {weights}')
            if 'varbins' in histogram.keys():
                histos[histname] = df_out.Histo1D(TM1(histname,
                                                      histname,
                                                      histogram['nbins'],
                                                      numpy.array(histogram['varbins'])),
                                                  branchname, 'w')
            else:
                histos[histname] = df_out.Histo1D(TM1(histname,
                                                      histname,
                                                      histogram['nbins'],
                                                      histogram['xmin'],
                                                      histogram['xmax']),
                                                  branchname, 'w')

            # apply global scale
            efficiency = histos[histname].GetEntries() / dataset_size
            scale = samples[sample]['XS'] * efficiency * samples[sample][year]['KFactor'] * lumi[year] / dataset_size
            histos[histname].Scale(scale)

            print(f"scaled with {scale:.3g} = {samples[sample]['XS']:.1f}(XS) * {efficiency}(efficiency) \
            * {samples[sample][year]['KFactor']}(K-factor) * {lumi[year]}(lumi) / {dataset_size}(Entries)")

        else:
            print(f'\n\n\tERROR: Branch "{branchname}" defined in config/histogram.py not found!\n')


    print('\n\n==============Config Summary===============')
    print('Systematic: {}'.format(systematic))
    print('Output: {}'.format(outFileName))
    print('Region: {}'.format(region))
    print('===========================================\n\n')

    print('\nFILLING HISTOGRAMS')

    report = df_out.Report()

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

    parser.add_argument('--sample', type=str, required=True,
                        help='sample to process')

    parser.add_argument('--systematic', type=str, default='nominal',
                        help='systematic to process')

    parser.add_argument('--cuts', action='store', default=[], nargs='+',
                        help='cuts to apply')


    args = parser.parse_args()

    print(f'Converting {args.sample}')

    fillhistos(year=args.year, region=args.region, sample=args.sample, systematic=args.systematic, cuts=args.cuts)
