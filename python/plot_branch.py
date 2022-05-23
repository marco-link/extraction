# -*- coding: utf-8 -*-

"""
Script to plot a single histogram.
View arguments with ``python python/plot_branch.py -h``.
"""

import os
import numpy
import argparse
import uproot
import matplotlib
import matplotlib.pyplot
import mplhep

from config.general import general, lumi, histopath
from config.data import data
from config.datasets import datasets, background
from config.histograms import histograms

matplotlib.use('Agg')
matplotlib.pyplot.style.use(mplhep.style.CMS)


def plot(year, region, systematic, histo, signal):
    """
    plot a histogram for a specific year, region and systematic.

    :param year: year
    :param region: region name
    :param systematic: systematic name
    :param histo: histo name
    """
    histogram = histograms[histo]

    fig = matplotlib.pyplot.figure(figsize=(12, 12))
    plot = fig.add_subplot(111)


    # data
    datahistos = []
    for dataset in data:
        with uproot.open(histopath(year=year,
                                   dataset=dataset,
                                   region=region,
                                   systematic=None)) as infile:
            datahistos.append(infile[general['Histodir']][histo].to_numpy())

    datahistos = numpy.array(datahistos, dtype=object)

    mplhep.histplot((numpy.sum(datahistos.T[0]), datahistos[0][1]),
                    ax=plot,
                    yerr=True,
                    histtype='errorbar',
                    color='k',
                    label='data',
                    density='density' in histogram['Plot'])

    # MC
    histos = []
    labels = []
    colors = []

    datasetlist = [signal] + list(background.keys())
    datasetlist.reverse()

    for dataset in datasetlist:
        if 'datasets' in histogram.keys() and dataset not in histogram['datasets']:
            print('Skipping histogram plotting for "{}" (histogram not defined for "{}" dataset)'.format(histo, dataset))
            continue

        with uproot.open(histopath(year=year,
                                   dataset=dataset,
                                   region=region,
                                   systematic=systematic)) as infile:

            histos.append(infile[general['Histodir']][histo])
            labels.append(datasets[dataset]['Label'])
            colors.append(datasets[dataset]['Color'])


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


    # visuals
    mplhep.cms.label(loc=1, ax=plot, data=False, paper=False, lumi=lumi[year])

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
        handles, labels = plot.get_legend_handles_labels()
        handles = [handles[-1]] + handles[:-1]
        labels = [labels[-1]] + labels[:-1]
        plot.legend(handles, labels, frameon=True, framealpha=0.4, edgecolor='w', loc=4)

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

    parser.add_argument('--systematic', type=str, default='nominal',
                        help='systematic to process')

    parser.add_argument('--histo', type=str, default='none',
                        help='trigger name')

    parser.add_argument('--signal', type=str, default='WbWbX_19',
                        help='signal variation')

    args = parser.parse_args()
    print(args)

    plot(year=args.year, region=args.region, systematic=args.systematic, histo=args.histo, signal=args.signal)
