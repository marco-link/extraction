#!/usr/bin/python
# -*- coding: utf-8 -*-

import datetime
import numpy
import argparse

from ROOT import TH1, ROOT, TFile

from helpers import getSystsplit, get_event_weigths
from config.general import general, samplepath, histopath, lumi
from config.samples import samples
from config.histograms import histograms
from config.systematics import systematics


TH1.SetDefaultSumw2(True)
TH1.StatOverflows(True)

# enable multi-threading
ROOT.EnableImplicitMT()
RDF = ROOT.RDataFrame
TM1 = ROOT.RDF.TH1DModel


def fillhistos(args):
    starttime = datetime.datetime.now()
    print('\nSTARTING AT {}'.format(str(starttime)))

    year = args.year
    sample = args.sample
    region = args.region
    systematic = args.systematic
    trigger = args.trigger
    print(trigger)
    cuts = args.cuts

    print('Year: {}'.format(year))
    print('Sample: {}'.format(sample))
    print('Region: {}'.format(region))
    print('Systematic: {}'.format(systematic))

    weights = get_event_weigths(year, sample, systematic)
    print('EventWeights: {}'.format(weights))

    inFileName = samplepath(isMC=samples[sample]['MC'], year=year, filename=samples[sample][year]['FileName'])
    outFileName = histopath(isMC=samples[sample]['MC'], year=year, filename=sample, region=region, systematic=systematic)


    print('\nOPENING INPUT FILE AND CREATING DATAFRAME')
    df_in = RDF(general['Tree'], inFileName)
    df_out = df_in

    for cut in cuts:
        if cut != 'none':
            print('Applying additional cut: {}'.format(cut))
            df_out = df_out.Filter(cut, cut)



    df_out = df_out.Define('w', weights)


    print('\nLOOPING OVER HISTOGRAMS')
    histos = {}
    for histname in histograms.keys():
        systematic, direction = getSystsplit(systematic)
        branchname = histograms[histname]['Branch']

        if 'Branch' in systematics[systematic].keys():
            branchname = systematics[systematic]['Branch'][direction] + '_' + branchname #FIXME
        else:
            branchname = 'nominal_' + branchname

        print(f'Reading from branch "{branchname}"...')


        if 'Samples' in histograms[histname].keys() and sample not in histograms[histname]['Samples']:
            print('Skipping histogram generation for "{}" (histogram not defined for this sample)'.format(histname))
            continue

        if 'Expression' in histograms[histname].keys():
            print('\nAdding temporary branch "{}" from Expression: {}'.format(histname, histograms[histname]['Expression']))
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
            efficiency = histos[histname].GetEntries() / samples[sample][year]['Entries']
            scale = samples[sample]['XS'] * efficiency * samples[sample][year]['KFactor'] * lumi[year] / samples[sample][year]['Entries']
            histos[histname].Scale(scale)

            print(f"scaled with {scale:.3g} = {samples[sample]['XS']:.1f}(XS) * {efficiency}(efficiency) \
* {samples[sample][year]['KFactor']}(K-factor) * {lumi[year]}(lumi) / {samples[sample][year]['Entries']}(Entries)")

        else:
            print('\n\n\tERROR: Branch "{}" defined in config/histogram.py not found!\n'.format(histname))


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

    parser.add_argument('--trigger', type=str, default='none',
                        help='trigger name')


    args = parser.parse_args()

    print('Converting {}'.format(args.sample))

    fillhistos(args)
