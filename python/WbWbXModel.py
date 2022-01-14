# -*- coding: utf-8 -*-

import numpy
import pandas
from HiggsAnalysis.CombinedLimit.PhysicsModel import PhysicsModelBase
#TODO documentation


class DefaultWbWbXModel(PhysicsModelBase):
    """
    Combine model for WbWbX fit with two parameters mtop and gammat
    """

    def __init__(self, verbose=False):
        self.verbose = verbose
        self.gen_json = pandas.read_json('config/xsecs.json').T
        self.minmass = self.gen_json['mass'].min()
        self.maxmass = self.gen_json['mass'].max()
        self.minwidth = self.gen_json['width'].min()
        self.maxwidth = self.gen_json['width'].max()


    def doParametersOfInterest(self):
        """Create POI out of signal strength and MH"""
        self.modelBuilder.doVar('r[1,0.0,10.0]')
        self.modelBuilder.doVar('m_top[172.5,{},{}]'.format(self.minmass, self.maxmass))
        self.modelBuilder.doVar('gamma_t[1.322,{},{}]'.format(self.minwidth, self.maxwidth))

        self.modelBuilder.doSet('POI', 'r,m_top,gamma_t')
        self.setup()


    def getGridRange(self, mtop, gammat):
        #"""
        #Who doesn't want some support?
        #Determines the support point in the mass/width grid.

        #:param mtop: value of the top mass TODO update docstring
        #:param gammat: value of the top width
        #:return: numpy array containing index and scale
        #"""
        masspoints = numpy.unique(self.gen_json['mass'])
        widthpoints = numpy.unique(self.gen_json['width'])

        lmass = self.minmass
        umass = self.maxmass
        lwidth = self.minwidth
        uwidth = self.maxwidth

        # if point not at border point select next grid point
        if mtop > lmass:
            lmass = masspoints[masspoints < mtop].max()
        if mtop < umass:
            umass = masspoints[masspoints > mtop].min()
        if gammat > lwidth:
            lwidth = widthpoints[widthpoints < gammat].max()
        if gammat < uwidth:
            uwidth = widthpoints[widthpoints > gammat].min()

        if self.verbose:
            print('----grid-----')
            print(mtop, gammat)
            print(lmass, umass)
            print(lwidth, uwidth)
            print('-------------')

        return [lmass, umass, lwidth, uwidth]


    def setup(self):
        last = None
        for i in self.gen_json.T:
            mtop = self.gen_json['mass'][i]
            gammat = self.gen_json['width'][i]
            limits = self.getGridRange(mtop=mtop, gammat=gammat)

            # switch off points unused points
            self.modelBuilder.factory_(('expr::Switch_WbWbX_{i}("(@0>{lmass})*'
                                        '(@0<{umass})*(@1>{lwidth})*(@1<{uwidth})",'
                                        'm_top, gamma_t)').format(i=i, lmass=limits[0], umass=limits[1],
                                                                  lwidth=limits[2], uwidth=limits[3]))

            # scaling linear with distance
            self.modelBuilder.factory_(('expr::Scaling_WbWbX_{i}("@0/(0.0000001 + '
                                        'sqrt((@1-{mass})*(@1-{mass}) + (@2-{width})*(@2-{width})))", '
                                        'Switch_WbWbX_{i}, m_top, gamma_t)').format(i=i, mass=mtop, width=gammat))

            # sum up all scales (doing it in one expression is too long for combine to handle)
            if last is None:
                self.modelBuilder.factory_('expr::Sum_WbWbX_{i}("@0", Scaling_WbWbX_{i})'.format(i=i))
            else:
                self.modelBuilder.factory_('expr::Sum_WbWbX_{i}("@0+@1", Scaling_WbWbX_{i}, {last})'.format(i=i, last=last))
            last = 'Sum_WbWbX_{}'.format(i)

        self.modelBuilder.factory_('expr::Normalization_WbWbX("@0/@1", r, {})'.format(last))


    def getYieldScale(self, bin, process):
        if 'WbWbX_' in process:
            self.modelBuilder.factory_('expr::FinalScale_{proc}("@0*@1", Scaling_{proc}, Normalization_WbWbX)'.format(proc=process))
            return 'FinalScale_' + process
        else:
            return 1


DefaultWbWbXModel = DefaultWbWbXModel()
