# -*- coding: utf-8 -*-

import luigi

from workflow.BaseTask import BaseTask
from workflow.FitTask import AllFitTasks

from config.general import general


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
        return [luigi.LocalTarget(f'{general["PlotPath"]}/{self.fitname}.pdf'),
                luigi.LocalTarget(self.log())]

    def run(self):
        """
        tasks runs :mod:`python/plot_NLL.py` and produces a logfile
        """
        self.save_execute(command=f'python python/plot_NLL.py {self.options} \
                                    --input {general["FitPath"]}/{self.fitname}/' + '{i}' + f'/NLLfit.root \
                                    --output {general["PlotPath"]}/{self.fitname}.pdf', log=self.log())
