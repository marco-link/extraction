# -*- coding: utf-8 -*-

"""
Script to plot the result of the NLL fit.
View arguments with ``python python/plot_NLL.py -h``.
"""

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

matplotlib.use('Agg')
matplotlib.pyplot.style.use(mplhep.style.CMS)




sigma = [1, 2, 3, 4, 5]


def getNLL(infile):
    """
    read NLL from root output of fit

    :param infile: file path to the fit output
    :returns: NLL from root file (``nll0+nll``)
    """
    with uproot.open(infile + ':limit') as tree:
        nll0 = tree['nll0'].array()[-1]
        nll = tree['nll'].array()[-1]

        print('{}: {:.3f}, {:.3f}'.format(infile, nll0, nll))

        return nll0 + nll


def bestfit(p, xdata, data):
    """
    determines best fit value and sigma intervals by interpolating given data.
    The result is added to the plot.

    :param p: subplot
    :param xdata: x values
    :param data: y values (should be NLL)
    """
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



if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', '-i', type=str, default='grid.root',
                        help='input files with NLL values')

    parser.add_argument('--output', '-o', type=str, default='plots',
                        help='output folder for plots')

    parser.add_argument('--nologo', action='store_true',
                        help='remove CMS logo')

    parser.add_argument('-verbose', '-v', action='store_true',
                        help='increase verbosity')

    parser.add_argument('--data', action='store_true',
                        help='plots contain data')

    parser.add_argument('--paper', action='store_true',
                        help='plot is for paper')

    parser.add_argument('--supplementary', action='store_true',
                        help='for supplementary plots')

    parser.add_argument('--lumi', '-l', type=float, default=-1,
                        help='luminosity')

    parser.add_argument('--SM', action='store', default=[1.322, 172.5], type=float, nargs='+',
                        help='SM point')

    parser.add_argument('--variables', action='store', default=['gamma_t', 'm_top'], nargs='+',
                        help='x/y variable names')

    parser.add_argument('--labels', action='store', default=[r'$\Gamma_t$', '$m_t$'], nargs='+',
                        help='x/y variable labels')

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


    tree = uproot.open(args.input + ':limit')
    if debug:
        tree.show()




    if len(args.variables) == 1:
        print('plotting 1D...\n\n')

        # remove duplicate points
        x, NLL = numpy.array([]), numpy.array([])
        for X, Y in zip(numpy.array(tree[args.variables[0]].array()), numpy.array(tree['deltaNLL'].array())):
            if X in x:
                pass
            else:
                x = numpy.append(x, [X])
                NLL = numpy.append(NLL, [2 * Y])

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
                p1.text(x.max(), s**2, r' ${}\sigma$'.format(s),
                        verticalalignment='center', horizontalalignment='left', size=18, alpha=0.5)

        #stamp_process(p1, inline=True)
        p1.legend(loc=1, frameon=True, edgecolor='w')
        p1.set_xlabel(args.labels[0], horizontalalignment='right', x=1.0)
        p1.set_ylabel(r'$-2\,\Delta\log(\mathcal{L})$', horizontalalignment='right', y=1.0)

        p1.text(0.98, 0.97, args.text, fontsize=20, transform=p1.transAxes, va='top', ha='right')


        if not args.nologo:
            mplhep.cms.label(ax=p1, data=args.data, paper=args.paper, lumi=args.lumi)


        fig.tight_layout()
        fig.savefig(args.output, dpi=300, transparent=False)



    elif len(args.variables) == 2:
        print('plotting 2D...\n\n')
        # remove duplicate points
        X, Y, NLL = numpy.array([]), numpy.array([]), numpy.array([])
        for x, y, z in zip(numpy.array(tree[args.variables[0]].array()),
                           numpy.array(tree[args.variables[1]].array()),
                           numpy.array(tree['deltaNLL'].array())):
            if x in X[Y == y]:
                pass
            else:
                X = numpy.append(X, [x])
                Y = numpy.append(Y, [y])
                NLL = numpy.append(NLL, [2 * z])



        NLLinterpolator = matplotlib.tri.LinearTriInterpolator(matplotlib.tri.Triangulation(X, Y), NLL)
        NLLinterpolator2 = matplotlib.tri.CubicTriInterpolator(matplotlib.tri.Triangulation(X, Y), NLL)

        xi = numpy.linspace(numpy.min(X), numpy.max(X), 500)
        yi = numpy.linspace(numpy.min(Y), numpy.max(Y), 500)
        zi = NLLinterpolator2(*numpy.meshgrid(xi, yi))


        if debug:
            for i in range(len(NLL)):
                print('{:.3f}, {:.3f}, {:.3f}'.format(X[i], Y[i], NLL[i]))




        fig = matplotlib.pyplot.figure(figsize=(11, 11))

        p1 = fig.add_subplot(111)



        levels = []
        fmt = {}
        for s in [1, 2, 3]:
            levels.append(s**2)
            fmt[s**2] = r'{:.0f}$\sigma$'.format(s)

        p1.contourf(xi, yi, zi, levels=[1, 4, 9, 16, 25, 36, 49, 1E9], cmap='YlOrRd', alpha=0.4, vmin=-1, vmax=49)
        p1.clabel(p1.contour(xi, yi, zi, levels, colors='k', linestyles=['-', '--', ':'], linewidths=1), fmt=fmt, fontsize=12, inline=True)
        p1.plot(args.SM[0], args.SM[1], 'bo', label='SM')

        p1.text(0.98, 0.97, args.text, fontsize=20, transform=p1.transAxes, va='top', ha='right')


        # find X0 from grid
        X0 = [X[NLL == numpy.min(NLL)][0], Y[NLL == numpy.min(NLL)][0]]

        res = scipy.optimize.minimize(lambda x: NLLinterpolator(*x), x0=X0, tol=1e-6, method='Nelder-Mead')
        print(res)

        if res.success:
            p1.plot(*res.x, 'r+', label='best fit\n${}={:.2f}$, ${}={:.2f}$'.format(args.labels[0].replace('$', ''),
                                                                                    res.x[0],
                                                                                    args.labels[1].replace('$', ''),
                                                                                    res.x[1]))

        if debug:
            p1.plot(X, Y, 'g,', label='grid points')

        #stamp_process(p1)
        p1.legend(loc=1, frameon=True, edgecolor='w')
        p1.set_xlabel(args.labels[0], horizontalalignment='right', x=1.0)
        p1.set_ylabel(args.labels[1], horizontalalignment='right', y=1.0)

        if not args.nologo:
            mplhep.cms.label(ax=p1, data=args.data, paper=args.paper, lumi=args.lumi)

        fig.tight_layout()
        fig.savefig(args.output, dpi=300, transparent=False)
