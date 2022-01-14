# -*- coding: utf-8 -*-

import luigi

from workflow.BaseTask import BaseTask
from workflow.HistoTask import AllHistoTasks

from config.general import general
from config.regions import regions


class DatacardTask(BaseTask):
    """
    A luigi task to produce datacards for different years/regions

    :param year: year for which to produce the plots
    :param region: region for which to produce the plots
    :param histogram: histogram for which to produce the plots
    """
    year = luigi.Parameter()
    region = luigi.Parameter()
    histogram = luigi.Parameter()

    def log(self):
        """
        defines output path for task logs in general log folder under ``datacard``
        """
        return f'{general["LogPath"]}/datacard/{self.year}/{self.region}/{self.histogram}.log'

    def requires(self):
        """
        task requires all histograms to be produced
        """
        return [AllHistoTasks(year=self.year)]

    def output(self):
        """
        tasks outputs a logfile and the datacard (.txt and .root file)
        """
        return [luigi.LocalTarget(f'./cards/{self.year}/{self.region}/{self.histogram}.txt'),
                luigi.LocalTarget(f'./cards/{self.year}/{self.region}/{self.histogram}.root'),
                luigi.LocalTarget(self.log())]

    def run(self):
        """
        tasks runs :mod:`python/build_cards.py` in combine environment and produces a logfile
        """
        self.save_execute(command=f'env -i sh scripts/execute_combine.sh "python2 python/build_cards.py \
            --year {self.year}\
            --region {self.region} \
            --shape {self.histogram} \
            --outpath ./cards/{self.year}/{self.region}/{self.histogram}.txt"', log=self.log())


class AllDatacardTasks(luigi.WrapperTask):
    """
    A luigi task to combine datacards from different years/regions
    """

    year = luigi.Parameter()
    histogram = luigi.Parameter()

    def requires(self):
        """
        defines required DatacardTasks
        """
        for region in regions.keys():
            yield DatacardTask(year=self.year, region=region, histogram=self.histogram)
