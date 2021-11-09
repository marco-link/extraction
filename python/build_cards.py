# -*- coding: utf-8 -*-

import argparse

import ROOT
import CombineHarvester.CombineTools.ch as ch
# see https://cms-analysis.github.io/CombineHarvester/python-interface.html

from config.general import general, histopath
from config.samples import background
from config.systematics import systematics

era = '13TeV'


def buildcard(args):
    bins = [(0, args.region)]

    parser = ch.CombineHarvester()

    # add observation
    parser.AddObservations(era=[era], bin=bins)

    # add MC
    parser.AddProcesses(procs=[args.signalprocess], era=[era], bin=bins, signal=True)
    parser.AddProcesses(procs=background.keys(), era=[era], bin=bins, signal=False)

    # fill with shapes
    def setShape(p):
        f = ROOT.TFile(histopath(isMC=True, year=args.year, filename=p.process(), region=p.bin(), systematic='nominal'), 'read')
        shape = f.Get(general['Histodir'] + '/' + args.shape)

        p.set_shape(shape, True)

    parser.ForEachProc(setShape)


    # add systematics
    for region in parser.bin_set():
        for syst in systematics:
            systematic = systematics[syst]

            if syst == 'nominal' or args.year not in systematic['years']:
                continue

            processes = parser.process_set()
            if 'samples' in systematic.keys():
                processes = systematic['samples']

            if systematic['type'] == 'shape':
                for process in processes:
                    print('adding systematic: ', process, syst)

                    s = ch.Systematic()
                    s.set_bin(region)
                    s.set_process(process)
                    s.set_era(era)
                    if process == args.signalprocess:
                        s.set_signal(True)

                    s.set_name(syst)
                    s.set_type('shape')

                    # fill shapes
                    f_nominal = ROOT.TFile(histopath(isMC=True, year=args.year, filename=process,
                                                     region=region, systematic='nominal'), 'read')
                    nominalinal = f_nominal.Get(general['Histodir'] + '/' + args.shape)

                    f_up = ROOT.TFile(histopath(isMC=True, year=args.year, filename=process,
                                                region=region, systematic=syst + 'UP'), 'read')
                    up = f_up.Get(general['Histodir'] + '/' + args.shape)

                    f_down = ROOT.TFile(histopath(isMC=True, year=args.year, filename=process,
                                                  region=region, systematic=syst + 'DOWN'), 'read')
                    down = f_down.Get(general['Histodir'] + '/' + args.shape)

                    s.set_shapes(up, down, nominalinal)
                    parser.InsertSystematic(s)
            elif systematic['type'] == 'lnN':
                parser.cp().process(processes).AddSyst(parser, syst, 'lnN', ch.SystMap()(systematic['value']))
            else:
                raise Exception('Unkown systematics type "{}"'.format(syst['type']))



    # AutoMCStats
    parser.SetAutoMCStats(parser, 10, False, 1)



    # TODO fill observation

    parser.PrintAll()
    ch.CardWriter(args.outpath, args.outpath.replace('.txt', '.root')).CreateDirectories(True).WriteCards('none', parser)







if __name__ == '__main__':
    argparser = argparse.ArgumentParser()

    argparser.add_argument('--outpath', type=str, default='./cards/datacard.txt',
                           help='output path of datacard')

    argparser.add_argument('--signalprocess', '-s', type=str, default='WbWbX_19',
                           help='signal process name')

    argparser.add_argument('--year', type=str, default='2016',
                           help='year of the datacard')

    argparser.add_argument('--region', type=str, default='muon',
                           help='region of the datacard')

    argparser.add_argument('--shape', type=str, default='Reco_Wb',
                           help='shape name')


    args = argparser.parse_args()
    print(args)

    buildcard(args)
