# -*- coding: utf-8 -*-

import law
import luigi

from workflow.BaseTask import BaseTask
from workflow.FitTask import AllFitTasks

from config.general import general

#TODO update documentation





class NLLPlotTask(BaseTask):
    """
    A luigi task to fperform the NLL fits

    :param fitname: unique name of the fit
    :param histogram: histogram for which to produce the plot
    :param cardmask: cardmask to select specific cards e.g. ``cards/<year or *>/<region or *>/<histogram>_{i}.txt``.
    :param options: extra options to give to the plotting script (see :mod:`python/plot_NLL.py`)
    """
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()
    options = luigi.Parameter(default='')


    def log(self):
        """
        defines output path for task logs in general log folder under ``NLLplot``
        """
        return f'{general["LogPath"]}/NLLplot/{self.fitname}.log'

    def requires(self):
        """
        task requires all fits to be completed before plotting
        """
        return AllFitTasks(fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask)

    def output(self):
        """
        tasks outputs a logfile and the plot inside the plotpath
        """
        return [law.LocalFileTarget(f'{general["PlotPath"]}/{self.fitname}.pdf'),
                law.LocalFileTarget(f'{general["PlotPath"]}/{self.fitname}_profiled.pdf'),
                law.LocalFileTarget(self.log()),
                law.LocalFileTarget(self.log().replace('.log', '_profiled.log'))]

    def run(self):
        """
        tasks runs :mod:`python/plot_NLL.py` and produces a logfile
        """
        self.save_execute(command=f'python python/plot_NLL.py {self.options} \
                                    --input {general["FitPath"]}/{self.fitname}/fit.root \
                                    --output {general["PlotPath"]}/{self.fitname}.pdf', log=self.log())

        self.save_execute(command=f'python python/plot_NLL.py {self.options} --variables gamma_t -v \
                                    --input {general["FitPath"]}/{self.fitname}/fit_profiled.root \
                                    --output {general["PlotPath"]}/{self.fitname}_profiled.pdf',
                          log=self.log().replace('.log', '_profiled.log'))
