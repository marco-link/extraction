# -*- coding: utf-8 -*-

import os
import argparse
import numpy
import uproot
import scipy.stats
import scipy.optimize
import scipy.interpolate

import matplotlib
import matplotlib.pyplot
import mplhep

from config.samples import gen_json

matplotlib.use('Agg')
matplotlib.pyplot.style.use(mplhep.style.CMS)




sigma = [1, 2, 3, 4, 5]


def getPrbfromStdev(x):
    if x < 0:
        raise ValueError('ERROR: standard deviation cannot be smaller than zero!')

    return scipy.stats.norm.cdf(x) - scipy.stats.norm.cdf(-x)


def getStdevfromPrb(x):
    if x < 0 or x >= 1:
        raise ValueError('ERROR: probability < 0 or >=1! Cannot calculate standard deviation.')

    return scipy.stats.norm.interval(x)[1]


def getNLL(infile):
    with uproot.open(infile + ':limit') as tree:
        nll0 = tree['nll0'].array()[-1]
        nll = tree['nll'].array()[-1]

        print('{}: {:.3f}, {:.3f}'.format(infile, nll0, nll))

        return nll0 + nll


def bestfit(p, xdata, data):
    if numpy.max(data) < 1.5:
        print('\n\nNO sensitivity! skipping best fit...\n')
        return False

    stat = {}

    def interpol(x, y, xint):
        spline = scipy.interpolate.splrep(x, y, s=0, k=1)
        return scipy.interpolate.splev(xint, spline)

    def obsLikelihood(z, shift=0):
        return interpol(xdata, data, z) - shift


    # determine best fit central value
    x0 = xdata[data == data.min()]
    if len(x0) > 1:
        x0 = x0[0]

    res = scipy.optimize.minimize(lambda x: obsLikelihood(x, shift=0), x0=x0, tol=1e-6, method='Nelder-Mead')
    print(res)

    stat['central'] = res.x[0]

    if res.success:
        for s in sigma:
            def lowerbound(x):
                if x < stat['central']:
                    return obsLikelihood(x, shift=s**2)**2
                else:
                    return numpy.exp(1 + (x - stat['central'])**2)

            def upperbound(x):
                if x > stat['central']:
                    return obsLikelihood(x, shift=s**2)**2
                else:
                    return numpy.exp(1 + (x - stat['central'])**2)

            # find startvalues for intersection by searching for signflip
            lowX0 = stat['central']
            for xdiff in numpy.linspace(0, 10, 1000):
                if obsLikelihood(lowX0, shift=s**2) * obsLikelihood(stat['central'] - xdiff, shift=s**2) < 0:
                    break
                else:
                    lowX0 = stat['central'] - xdiff

            upX0 = stat['central']
            for xdiff in numpy.linspace(0, 10, 1000):
                if obsLikelihood(upX0, shift=s**2) * obsLikelihood(stat['central'] + xdiff, shift=s**2) < 0:
                    break
                else:
                    upX0 = stat['central'] + xdiff


            low = scipy.optimize.minimize(lowerbound, x0=lowX0, tol=1e-6, method='Nelder-Mead')
            up = scipy.optimize.minimize(upperbound, x0=upX0, tol=1e-6, method='Nelder-Mead')

            stat['{} sigma'.format(s)] = [low.x[0], up.x[0]]

        if debug:
            for s in sigma:
                p1.plot(stat['{} sigma'.format(s)], obsLikelihood(stat['{} sigma'.format(s)], shift=0), 'ko-', )

        for s in stat:
            print('{}: {}'.format(s, stat[s]))


        p.plot([stat['central'], stat['central']], [0, ymax], 'k-', lw=0.8,
               label=f'best fit\n$\\Gamma_t={stat["central"]:.2f}\\,\
                        ^{{+{stat["1 sigma"][1] - stat["central"]:.2f}}}\
                        _{{-{stat["central"] - stat["1 sigma"][0]:.2f}}}$')

        p.axvspan(*stat['2 sigma'], facecolor='yellow', alpha=0.8, lw=0, label=r'best fit $\pm$ 2 std. dev.')
        p.axvspan(*stat['1 sigma'], facecolor='lime', alpha=0.8, lw=0, label=r'best fit $\pm$ 1 std. dev.')




parser = argparse.ArgumentParser()
parser.add_argument('--input', '-i', type=str, default='./fits/all/{i}/NLLfit.root',
                    help='input files with NLL values')

parser.add_argument('--output', '-o', type=str, default='./NLL.pdf',
                    help='output name for plot')

parser.add_argument('--nologo', action='store_true',
                    help='remove CMS logo')

parser.add_argument('--verbose', '-v', action='store_true',
                    help='increase verbosity')

parser.add_argument('--data', action='store_true',
                    help='plots contain data')

parser.add_argument('--paper', action='store_true',
                    help='plots is for paper')

parser.add_argument('--supplementary', action='store_true',
                    help='plots supplementary')

parser.add_argument('--lumi', type=float, default=-1,
                    help='luminosity')

parser.add_argument('--text', type=str, default='',
                    help='text put into the plot')

parser.add_argument('--ymax', type=float, default=30,
                    help='y axis upper limit')



args = parser.parse_args()
print(args)
print()
debug = args.verbose
ymax = args.ymax

os.makedirs(os.path.dirname(args.output), exist_ok=True)


x, NLL = [], []
for index in gen_json.keys():
    x.append(gen_json[index]['width'])
    NLL.append(2 * getNLL(args.input.format(i=index)))

x = numpy.array(x)
NLL = numpy.array(NLL)
NLL = NLL - NLL.min()

idx = numpy.argsort(x)
x, NLL = x[idx], NLL[idx]




fig = matplotlib.pyplot.figure()
p1 = fig.add_subplot(111)


p1.plot(x, NLL, 'b:', label='expected')
bestfit(p1, x, NLL)

if debug:
    p1.plot(x, NLL, 'g.', label='points')



p1.set_xlim(x.min(), x.max())
p1.set_ylim(0, ymax)
for s in sigma:
    p1.plot([x.min(), x.max()], [s**2, s**2], 'k-', lw=0.6, alpha=0.3)
    if s**2 < ymax:
        p1.text(x.max(), s**2, r' ${}\sigma$'.format(s), verticalalignment='center', horizontalalignment='left', size=18, alpha=0.5)

p1.legend(loc=1, frameon=True, edgecolor='w')
p1.set_xlabel(r'$\Gamma_t$ in GeV', horizontalalignment='right', x=1.0)
p1.set_ylabel(r'$-2\,\Delta\log(\mathcal{L})$', horizontalalignment='right', y=1.0)

p1.text(0.02, 0.98, args.text, fontsize=20, transform=p1.transAxes, va='top', ha='left')

if not args.nologo:
    mplhep.cms.label(ax=p1, data=args.data, paper=args.paper, supplementary=args.supplementary, lumi=args.lumi)

fig.tight_layout()
fig.savefig(args.output, dpi=300, transparent=False)
