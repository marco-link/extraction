# -*- coding: utf-8 -*-

import argparse
import uproot
import matplotlib
import matplotlib.pyplot
import mplhep

from config.general import general, histopath
from config.samples import samples
from config.histograms import histograms

matplotlib.use('Agg')
matplotlib.pyplot.style.use(mplhep.style.CMS)


def plot(args):
    histo = histograms[args.histo]

    fig = matplotlib.pyplot.figure()
    plot = fig.add_subplot(111)

    histos = []
    labels = []
    colors = []

    samplelist = list(samples.keys())
    samplelist.reverse()
    for sample in samplelist:
        if 'Samples' in histo.keys() and sample not in histo['Samples']:
            print('Skipping histogram plotting for "{}" (histogram not defined for "{}" sample)'.format(args.histo, sample))
            continue

        infile = uproot.open(histopath(isMC=samples[sample]['MC'],
                                       year=args.year,
                                       filename=sample,
                                       region=args.region,
                                       systematic=args.systematic))

        histos.append(infile[general['Histodir']][args.histo])
        labels.append(samples[sample]['Label'])
        colors.append(samples[sample]['Color'])

    mplhep.histplot(histos, ax=plot, stack=True, histtype='fill', color=colors, label=labels)
    mplhep.cms.label(ax=plot, data=False, paper=False, lumi=general['Lumi'][args.year])

    if 'Title' in histo.keys():
        plot.set_title(histo['Title'])
    else:
        plot.set_title(args.histo)

    if 'Xlabel' in histo.keys():
        plot.set_xlabel(histo['Xlabel'], x=1.0, ha='right')
    else:
        plot.set_xlabel(args.histo, x=1.0, ha='right')
    plot.set_ylabel('entries', verticalalignment='bottom', y=1.0) # TODO find out what i am plotting

    if 'xmin' in histo['Histogram'].keys():
        plot.set_xlim(histo['Histogram']['xmin'], histo['Histogram']['xmax'])

    plot.legend()


    fig.tight_layout()
    fig.savefig('{}.pdf'.format(args.histo), dpi=300)
    #matplotlib.pyplot.show()
    matplotlib.pyplot.close()



if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--year', type=str, required=True,
                        help='year to process')

    parser.add_argument('--region', type=str, required=True,
                        help='region to process')

    parser.add_argument('--systematic', type=str, default='nom',
                        help='systematic to process')

    parser.add_argument('--histo', type=str, default='none',
                        help='trigger name')

    #TODO logfile


    args = parser.parse_args()
    print(args)

    plot(args)
