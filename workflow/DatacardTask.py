# -*- coding: utf-8 -*-
"""
A luigi task to generate datacards
"""
import luigi

from workflow.BaseTask import BaseTask
from workflow.HistoTask import AllHistoTasks

from config.samples import gen_json


class DatacardTask(BaseTask):
    year = luigi.Parameter()
    histogram = luigi.Parameter()
    signal = luigi.Parameter()

    def log(self):
        return f'./logs/datacard/{self.year}/{self.histogram}/{self.signal}.log'

    def requires(self):
        return [AllHistoTasks(year=self.year)]

    def output(self):
        return [luigi.LocalTarget(f'./cards/{self.year}_{self.histogram}_{self.signal}.txt'),
                luigi.LocalTarget(f'./cards/{self.year}_{self.histogram}_{self.signal}.root'),
                luigi.LocalTarget(self.log())]

    def run(self):
        self.save_execute(command=f'env -i sh scripts/cards.sh --year {self.year} --shape {self.histogram} --signalprocess {self.signal} \
                                    --outpath ./cards/{self.year}_{self.histogram}_{self.signal}.txt', log=self.log())


class AllDatacardTasks(luigi.WrapperTask):
    year = luigi.Parameter()
    histogram = luigi.Parameter()

    def requires(self):
        for index in gen_json.keys():
            yield DatacardTask(year=self.year, histogram=self.histogram, signal='WbWbX_{}'.format(index))
