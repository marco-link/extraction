# -*- coding: utf-8 -*-

import luigi

from workflow.BaseTask import BaseTask

from config.general import general, histopath
from config.samples import samples
from config.regions import regions
from config.systematics import systematics


class HistoTask(BaseTask):
    """
    A luigi task to produce histograms

    :param year: year for which to produce the histograms
    :param sample: sample for which to produce the histograms
    :param region: region for which to produce the histograms
    :param systematic: systematic for which to produce the histograms
    """
    year = luigi.Parameter()
    sample = luigi.Parameter()
    region = luigi.Parameter()
    systematic = luigi.Parameter()

    def log(self):
        """
        defines output path for task logs in general log folder under ``fill_histos``
        """
        return f'{general["LogPath"]}/fill_histos/{self.year}/{self.region}/{self.systematic}/{self.sample}.log'

    def output(self):
        """
        tasks outputs a logfile and a root file inside the path from :func:`config.general.histopath`, containing the histogram
        """
        return [luigi.LocalTarget(self.log()),
                luigi.LocalTarget(histopath(isMC=samples[self.sample]['MC'],
                                            year=self.year,
                                            filename=self.sample,
                                            region=self.region,
                                            systematic=self.systematic))]

    def run(self):
        """
        tasks runs :mod:`python/fill_histos.py` and produces a logfile
        """
        self.save_execute(command=f'python python/fill_histos.py --year {self.year} --sample {self.sample} \
                                    --region {self.region} --systematic {self.systematic}', log=self.log())



class AllHistoTasks(luigi.WrapperTask):
    """
    A luigi wrapper task to produce all histograms

    :param year: year for which to produce the histograms
    """
    year = luigi.Parameter()

    def requires(self):
        """
        defines required HistoTasks
        """
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
