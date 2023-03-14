# -*- coding: utf-8 -*-

import law
import luigi
import glob

from workflow.BaseTask import BaseTask
from workflow.HistoTask import HistoTask

from helpers import histopath
from config.regions import regions
from config.datasets import datasetgroups


class MergeHistoTask(BaseTask):
    """
    A task merge histograms

    :param year: year to merge
    :param region: region to merge
    :param group: group of the dataset to merge
    """
    year = luigi.Parameter()
    region = luigi.Parameter()
    group = luigi.Parameter()

    def requires(self):
        """
        task requires all histograms to be produced
        """
        return [HistoTask(year=self.year)]

    def output(self):
        """
        tasks outputs a logfile and the merged root file
        """
        return [law.LocalFileTarget(histopath(self.year, self.region, self.group))]

    def run(self):
        """
        tasks runs `hadd` and produces a logfile
        """

        target = histopath(self.year, self.region, self.group)
        srcfiles = []
        for dataset in datasetgroups[self.group]:
            src = histopath(self.year, self.region, dataset).replace('.root', '_*.root')
            srcfiles += glob.glob(src)

        if len(srcfiles) > 1:
            self.execute(command=f'hadd -f {target} {" ".join(srcfiles)}')
        else:
            self.execute(command=f'ln -s {srcfiles[0]} {target}')



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
            for group in datasetgroups:
                yield MergeHistoTask(year=self.year, region=region, group=group)
