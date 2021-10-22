# -*- coding: utf-8 -*-
"""
A luigi task to fill histograms
"""
import luigi

from workflow.BaseTask import BaseTask

from config.general import histopath
from config.samples import samples
from config.regions import regions
from config.systematics import systematics


class HistoTask(BaseTask):
    year = luigi.Parameter()
    sample = luigi.Parameter()
    region = luigi.Parameter()
    systematic = luigi.Parameter()

    def log(self):
        return f'./logs/fill_histos/{self.year}/{self.region}/{self.systematic}/{self.sample}.log'

    def output(self):
        return [luigi.LocalTarget(self.log()),
                luigi.LocalTarget(histopath(isMC=samples[self.sample]['MC'],
                                            year=self.year,
                                            filename=self.sample,
                                            region=self.region,
                                            systematic=self.systematic))]

    def run(self):
        self.save_execute(command=f'python python/fill_histos.py --year {self.year} --sample {self.sample} \
                                    --region {self.region} --systematic {self.systematic}', log=self.log())



class AllHistoTasks(luigi.WrapperTask):
    year = luigi.Parameter()

    def requires(self):
        for sample in samples.keys():
            for region in regions.keys():
                for systematic in systematics.keys():
                    if systematics[systematic]['type'] == 'shape' and self.year in systematics[systematic]['years']:
                        if 'samples' not in systematics[systematic].keys() or sample in systematics[systematic]['samples']:
                            if systematic == 'nominal':
                                yield HistoTask(year=self.year, sample=sample, region=region, systematic=systematic)
                            else:
                                yield HistoTask(year=self.year, sample=sample, region=region, systematic=systematic + 'UP')
                                yield HistoTask(year=self.year, sample=sample, region=region, systematic=systematic + 'DOWN')
