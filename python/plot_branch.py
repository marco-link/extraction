# -*- coding: utf-8 -*-

"""
Script to plot a single histogram.
View arguments with ``python python/plot_branch.py -h``.
"""

import os
import argparse
import uproot
import matplotlib
import matplotlib.pyplot
import mplhep

from config.general import general, lumi, histopath
from config.samples import samples
from config.histograms import histograms

matplotlib.use('Agg')
matplotlib.pyplot.style.use(mplhep.style.CMS)


def plot(year, region, systematic, histo):
    """
    plot a histogram for a specific year, region and systematic.

    :param year: year
    :param region: region name
    :param systematic: systematic name
    :param histo: histo name
    """
    histogram = histograms[histo]

    fig = matplotlib.pyplot.figure()
    plot = fig.add_subplot(111)

    histos = []
    labels = []
    colors = []

    samplelist = list(samples.keys())
    samplelist.reverse()
    for sample in samplelist:
        if 'Samples' in histogram.keys() and sample not in histogram['Samples']:
            print('Skipping histogram plotting for "{}" (histogram not defined for "{}" sample)'.format(histo, sample))
            continue

        with uproot.open(histopath(isMC=samples[sample]['MC'],
                                   year=year,
                                   filename=sample,
                                   region=region,
                                   systematic=systematic)) as infile:

            histos.append(infile[general['Histodir']][histo])
            labels.append(samples[sample]['Label'])
            colors.append(samples[sample]['Color'])


    histtype = 'fill'
    if 'step' in histogram['Plot']:
        histtype = 'step'
    elif 'errorbar' in histogram['Plot']:
        histtype = 'errorbar'

    mplhep.histplot(histos,
                    ax=plot,
                    stack='nostack' not in histogram['Plot'],
                    histtype=histtype,
                    color=colors,
                    label=labels,
                    density='density' in histogram['Plot'])
    mplhep.cms.label(ax=plot, data=False, paper=False, lumi=lumi[year])

    if 'Title' in histogram.keys():
        plot.set_title(histogram['Title'])
    else:
        plot.set_title(histo)

    if 'Xlabel' in histogram.keys():
        plot.set_xlabel(histogram['Xlabel'], x=1.0, ha='right')
    else:
        plot.set_xlabel(histo, x=1.0, ha='right')

    if 'density' in histogram['Plot']:
        plot.set_ylabel('density', verticalalignment='bottom', y=1.0)
    else:
        plot.set_ylabel('entries', verticalalignment='bottom', y=1.0)

    if 'xmin' in histogram['Histogram'].keys():
        plot.set_xlim(histogram['Histogram']['xmin'], histogram['Histogram']['xmax'])

    if 'nolegend' not in histogram['Plot']:
        plot.legend()

    if 'logX' in histogram['Plot']:
        plot.set_xscale('log')

    if 'logY' in histogram['Plot']:
        plot.set_yscale('log')

    path = general['PlotPath'] + f'/{year}/{region}/{systematic}/'
    os.makedirs(path, exist_ok=True)

    fig.tight_layout()
    fig.savefig(path + f'{histo}.pdf', dpi=300)
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

    plot(year=args.year, region=args.region, systematic=args.systematic, histo=args.histo)
