# -*- coding: utf-8 -*-
"""
A luigi task to fperform the NLL fits
"""
import luigi

from workflow.BaseTask import BaseTask
from workflow.FitTask import AllFitTasks

from config.general import general


class NLLPlotTask(BaseTask):
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()
    options = luigi.Parameter(default='')


    def log(self):
        return f'{general["LogPath"]}/NLLplot/{self.fitname}.log'

    def requires(self):
        return AllFitTasks(fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask)

    def output(self):
        return [luigi.LocalTarget(f'{general["PlotPath"]}/{self.fitname}.pdf'),
                luigi.LocalTarget(self.log())]

    def run(self):
        self.save_execute(command=f'python python/plot_NLL.py {self.options} \
                                    --input {general["FitPath"]}/{self.fitname}/' + '{i}' + f'/NLLfit.root \
                                    --output {general["PlotPath"]}/{self.fitname}.pdf', log=self.log())
