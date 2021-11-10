# -*- coding: utf-8 -*-
"""
A luigi task to combine datacards from different years/regions
"""
import luigi
import glob
import os

from workflow.BaseTask import BaseTask
from workflow.DatacardTask import AllDatacardTasks

from config.general import general, allyears


class CombineCardTask(BaseTask):
    cardmask = luigi.Parameter()
    cardoutput = luigi.Parameter()
    histogram = luigi.Parameter()


    def log(self):
        return f'{general["LogPath"]}/combineCards/{self.cardoutput}.log'

    def requires(self):
        return [AllDatacardTasks(year=y, histogram=self.histogram) for y in allyears]

    def output(self):
        return [luigi.LocalTarget(self.cardoutput),
                luigi.LocalTarget(self.log())]

    def run(self):
        os.makedirs(os.path.dirname(self.cardoutput), exist_ok=True)
        files = ' '.join([f'.={f}' for f in glob.glob(self.cardmask, recursive=True)])
        self.save_execute(command=f'env -i sh scripts/combineCards.sh "{files}" {self.cardoutput}', log=self.log())
