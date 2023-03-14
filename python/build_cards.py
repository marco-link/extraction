# -*- coding: utf-8 -*-

"""
Run as script to produce datacards, requires environment with
`CombineHarvester <https://cms-analysis.github.io/CombineHarvester/python-interface.html>`_.
View arguments with ``python2 python/build_cards.py -h``.
"""

import argparse

import ROOT
import CombineHarvester.CombineTools.ch as ch
# see https://cms-analysis.github.io/CombineHarvester/python-interface.html

from helpers import histopath
from config.datasets import signal, datasetgroups
from config.systematics import systematics

era = '13TeV'


def buildcard(outpath, year, region, shape):
    """
    builds datacard

    :param outpath: output path for datacard
    :param year: year to build card for
    :param region: region to build card for
    :param shape: shape to build card for
    """
    print('building card "{}" for {}, {}, {}...'.format(outpath, year, region, shape))


    bins = [(0, region + '_' + year)]

    parser = ch.CombineHarvester()

    # add MC
    parser.AddProcesses(procs=signal.keys(), era=[era], bin=bins, signal=True)

    for process in datasetgroups.keys():
        if process not in signal.keys() and process != 'data':
            parser.AddProcesses(procs=[process], era=[era], bin=bins, signal=False)

    # fill with shapes
    def setShape(p):
        inroot = ROOT.TFile(histopath(year=year, region=region, dataset=p.process()), 'read')
        s = inroot.Get('nominal/' + shape)
        p.set_shape(s, True)
        inroot.Close()

    parser.ForEachProc(setShape)


    # add systematics
    processes = parser.process_set()
    for process in processes:
        inroot = ROOT.TFile(histopath(year=year, region=region, dataset=process), 'read')
        for syst in systematics:
            systematic = systematics[syst]

            if syst == 'nominal' or year not in systematic['years']:
                continue

            if 'datasets' in systematic.keys():
                processes = systematic['datasets']

            if systematic['type'] == 'shape':
                print('adding systematic: ', process, syst)

                s = ch.Systematic()
                s.set_bin(bins[0][1])
                s.set_process(process)
                s.set_era(era)
                if process in signal.keys():
                    s.set_signal(True)

                s.set_name(syst)
                s.set_type('shape')

                # fill shapes
                nominal = inroot.Get('nominal/' + shape)
                up = inroot.Get(syst + 'Up/' + shape)
                down = inroot.Get(syst + 'Down/' + shape)

                s.set_shapes(up, down, nominal)
                parser.InsertSystematic(s)
            elif systematic['type'] == 'lnN':
                parser.cp().process(processes).AddSyst(parser, syst, 'lnN', ch.SystMap()(systematic['value']))
            else:
                raise Exception('Unkown systematics type "{}"'.format(syst['type']))

        inroot.Close()

    # AutoMCStats
    parser.SetAutoMCStats(parser, 10, False, 1)


    # add observation
    print('adding observation...')
    inroot = ROOT.TFile(histopath(year=year, region=region, dataset='data'), 'read')

    obs = ch.Observation()
    obs.set_bin(region + '_' + year)
    #obs.set_process(process)
    obs.set_era(era)
    obs.set_shape(inroot.Get('None/' + shape), True)

    parser.InsertObservation(obs)
    inroot.Close()



    parser.PrintAll()
    ch.CardWriter(outpath, outpath.replace('.txt', '.root')).CreateDirectories(True).WriteCards('none', parser)




if __name__ == '__main__':
    argparser = argparse.ArgumentParser()

    argparser.add_argument('--outpath', type=str, default='./cards/datacard.txt',
                           help='output path of datacard')

    argparser.add_argument('--year', type=str, default='2016',
                           help='year of the datacard')

    argparser.add_argument('--region', type=str, default='muon',
                           help='region of the datacard')

    argparser.add_argument('--shape', type=str, default='Reco_Wb',
                           help='shape name')


    args = argparser.parse_args()
    print(args)

    buildcard(outpath=args.outpath,
              year=args.year,
              region=args.region,
              shape=args.shape)
