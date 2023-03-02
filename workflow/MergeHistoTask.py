# -*- coding: utf-8 -*-

import law
import luigi
import glob

from workflow.BaseTask import BaseTask
from workflow.HistoTask import HistoTask

from helpers import histopath
from config.regions import regions
from config.data import data
from config.datasets import datasets


class MergeHistoTask(BaseTask):
    """
    A task merge histograms

    :param year: year for which to produce the plots
    :param region: region for which to produce the plots
    """
    year = luigi.Parameter()
    region = luigi.Parameter()
    dataset = luigi.Parameter()

    def requires(self):
        """
        task requires all histograms to be produced
        """
        return [HistoTask(year=self.year)]

    def output(self):
        """
        tasks outputs a logfile and the merged root file
        """
        return [law.LocalFileTarget(histopath(self.year, self.region, self.dataset))]

    def run(self):
        """
        tasks runs `hadd` and produces a logfile
        """

        target = histopath(self.year, self.region, self.dataset)
        src = target.replace('.root', '_*.root')

        files = glob.glob(src)
        print(files)

        if len(files) > 1:
            self.execute(command=f'hadd -f {target} {src}')
        else:
            self.execute(command=f'ln -s {files[0]} {target}')



class AllMergeHistoTasks(law.WrapperTask):
    """
    A wrapper task to merge all histograms for all regions and systematic variations of a specific year

    :param year: year of the histograms to merge
    """
    year = luigi.Parameter()

    def requires(self):
        """
        defines required BranchPlotTasks
        """
        for region in regions.keys():
            # data merging
            for dataset in data.keys():
                yield MergeHistoTask(year=self.year, region=region, dataset=dataset)

            for dataset in datasets.keys():
                yield MergeHistoTask(year=self.year, region=region, dataset=dataset)
