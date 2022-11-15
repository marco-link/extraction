#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script using :mod:`Root.RDataFrame` to produce histograms.
View arguments with ``python python/fill_histos.py -h``.
"""

import datetime
import argparse

from ROOT import TH1, ROOT, TFile

from helpers import getSystsplit, getDatasetInfo, getGridpaths, histopath, get_event_weigths
from config.general import general, lumi
from config.data import data as datasamples
from config.datasets import datasets as mcsamples
from config.regions import regions
from config.histograms import histograms
#from config.systematics import systematics as global_syst_dict

allsamples = mcsamples.copy()
allsamples.update(datasamples)

TH1.SetDefaultSumw2(True)
TH1.StatOverflows(True)

RDF = ROOT.RDataFrame
TM1 = ROOT.RDF.TH1DModel

if general['EnableImplicitMT']:
    ROOT.EnableImplicitMT()


def create_input_info(year, region, dataset_key, process_systematics: list, number: int):
    '''
    global information on the dataset
    '''
    gridpaths = getGridpaths(year=year, setname=allsamples[dataset_key]['FileName'])
    preskimInfo = getDatasetInfo(year, dataset_key)

    w = {}
    for systematic in process_systematics:
        outfile = histopath(year=year,
                            region=region,
                            dataset=dataset_key,
                            systematic=systematic,
                            number=number)

        filter = None
        if 'Filter' in regions[region].keys():
            filter = regions[region]['Filter']
            if allsamples[dataset_key]['MC']:
                filter = filter.replace('nominal', systematic)

        w[systematic] = {'weight_sel_string': get_event_weigths(year, dataset_key, systematic, preskimInfo),
                         'temp_branch_name': 'w_' + systematic,
                         'region_filter': filter,
                         'region': region,
                         'outputFile': outfile}

        print(systematic, 'weight_sel_string', w[systematic]['weight_sel_string'])

    inFileName = gridpaths[number]
    return inFileName, w


def fillhistos(year, region, dataset_key, process_systematics, number, cuts=[], event_limit=None, verbose=True):
    """
    fill histograms

    :param year: year
    :param region: region name
    :param dataset_key: dataset key
    :param process_systematics: systematic name (can be list)
    :param number: file number
    :param cuts: cuts to apply
    """
    starttime = datetime.datetime.now()
    if verbose:
        print(f'\nSTARTING AT {str(starttime)}')

        print(f'Year: {year}')
        print(f'dataset key: {dataset_key}')
        print(f'Region: {region}')
        print(f'Systematics: {process_systematics}')

        # get configuration for all process_systematics
        print('\nCREATING PRESKIM INFO', year, region, dataset_key, process_systematics, number, datetime.datetime.now())

    inFileName, systematics_config = create_input_info(year, region, dataset_key, process_systematics, number)

    if verbose:
        print('\nOPENING INPUT FILE AND CREATING DATAFRAME FROM', inFileName, datetime.datetime.now())
    global_dataframe = RDF(general['Tree'], inFileName)

    # only here reduce so it also applies to weights
    if event_limit is not None:
        global_dataframe = global_dataframe.Range(event_limit)

    #this is global
    for cut in cuts:
        if cut != 'none':
            if verbose:
                print(f'Applying additional cut: {cut}')
            global_dataframe = global_dataframe.Filter(cut, cut)

    #add systematics also to global
    for systematic in process_systematics:
        sc = systematics_config[systematic]
        global_dataframe = global_dataframe.Define(sc['temp_branch_name'],
                                                   sc['weight_sel_string'])

    ### global dataframe prepared, can eneter process_systematics and histogram definition loop

    #just a list of: ( outfile,  dict of { histname: df_histo })
    histos_and_outfiles = []
    for systematic in process_systematics:
        sc = systematics_config[systematic]

        dataframe = global_dataframe
        dataframe = dataframe.Filter(sc['region_filter'], sc['region'])

        histos = {}
        if verbose:
            print('\nLOOPING OVER HISTOGRAMS FOR', systematic, datetime.datetime.now())

        for histname in histograms.keys():
            base_systematic, direction = getSystsplit(systematic)
            branchname = histograms[histname]['Branch']
            if verbose:
                print('original branch name', branchname)

            if allsamples[dataset_key]['MC']:
                branchname = histograms[histname]['Branch'].replace('nominal', systematic)
                if verbose:
                    print('adapted branch name', branchname)
                # WHY??
                #if 'Branch' in global_syst_dict[base_systematic].keys():
                #    branchname = branchname.replace('nominal', global_syst_dict[base_systematic]['Branch'][direction])
                #    print('double replace',branchnameå)
            if verbose:
                print(f'Reading from branch "{branchname}"...', systematic)

            if 'datasets' in histograms[histname].keys() and dataset_key not in histograms[histname]['datasets']:
                print(f'Skipping histogram generation for "{histname}" (histogram not defined for this dataset)')
                continue

            if 'Expression' in histograms[histname].keys():
                expression = histograms[histname]['Expression']
                if allsamples[dataset_key]['MC']:
                    expression = expression.replace('nominal', systematic)
                if verbose:
                    print(f'\nAdding temporary branch "{histname}" from Expression: {expression}')
                dataframe = dataframe.Define(branchname, expression)

            if branchname in dataframe.GetColumnNames():
                histogram = {}
                if 'Histogram' in histograms[histname].keys():
                    histogram = histograms[histname]['Histogram']

                if verbose:
                    print(f'Adding histogram for {histname} with weights', sc['weight_sel_string'])
                if 'varbins' in histogram.keys():
                    histos[histname] = dataframe.Histo1D(TM1(histname,
                                                             histname,
                                                             nbinsx=len(histogram['varbins']) - 1,
                                                             xbins=histogram['varbins']),
                                                         branchname,
                                                         sc['temp_branch_name'])
                else:
                    histos[histname] = dataframe.Histo1D(TM1(histname,
                                                             histname,
                                                             histogram['nbins'],
                                                             histogram['xmin'],
                                                             histogram['xmax']),
                                                         branchname,
                                                         sc['temp_branch_name'])


                # do not ask for the histogram entries or anything that requires processing
                # the ntuple at this step!!!
            else:
                print(f'\n\n\tERROR: Branch "{branchname}" defined in config/histogram.py not found!\n')

        histos_and_outfiles.append((sc['outputFile'], histos))
        if verbose:
            print('\n\n==============Config Summary===============')
            print('Systematic: {}'.format(systematic))
            print('Output: {}'.format(sc['outputFile']))
            print('Region: {}'.format(region))
            print('===========================================\n\n')


    if verbose:
        print('\nFILLING HISTOGRAMS')

    scale = 1.
    if allsamples[dataset_key]['MC']:
        scale = 1000 * allsamples[dataset_key]['XS'] * allsamples[dataset_key][year]['KFactor'] * lumi[year]


    for hao in histos_and_outfiles:
        outFileName = hao[0]
        processed_histograms = hao[1]
        if verbose:
            print('starting', outFileName, 'at', datetime.datetime.now())

        for histname in processed_histograms.keys():
            processed_histograms[histname].Scale(scale)
            #print(f'selected {histos[histname].GetEntries()} events out of {preskimInfo["genEventCount"]} (genEventCount)')
            #print(f"scaled with {scale:.3g} = {1000*datasets[dataset_key]['XS']:.1f}(XS in fb) * \
            #{datasets[dataset_key][year]['KFactor']}(K-factor) * {lumi[year]}(lumi in 1/fb)")

        #print('\nREPORT')
        #report = dataframe.Report()

        #overwrite
        outFile = TFile(outFileName, 'RECREATE')
        histoDir = outFile.Get(general['Histodir'])
        if not histoDir:
            histoDir = outFile.mkdir(general['Histodir'])
        histoDir.cd()
        for histogram in sorted(processed_histograms.keys()):
            histoDir.Append(processed_histograms[histogram].GetPtr(), True)
        histoDir.Write('', TFile.kOverwrite)
        outFile.Close()
        if verbose:
            print('OUTPUT WRITTEN TO {}'.format(outFileName))

    #print('\n\n==============Selection Efficiencies===============')
    #report.Print()

    endtime = datetime.datetime.now()
    if verbose:
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

    process_systematics = args.systematic.split(',')

    print(f'Converting {args.dataset}')

    fillhistos(year=args.year,
               region=args.region,
               dataset_key=args.dataset,
               process_systematics=process_systematics,
               number=args.number,
               cuts=args.cuts)
