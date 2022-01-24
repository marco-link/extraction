# -*- coding: utf-8 -*-

import law
import luigi

from workflow.BaseTask import BaseTask
from workflow.HistoTask import AllHistoTasks

from config.general import general
from config.histograms import histograms
from config.regions import regions
from config.systematics import systematics


class BranchPlotTask(BaseTask):
    """
    A task to plot histograms

    :param year: year for which to produce the plots
    :param region: region for which to produce the plots
    :param systematic: systematic for which to produce the plots
    :param histogram: histogram for which to produce the plots
    """
    year = luigi.Parameter()
    region = luigi.Parameter()
    systematic = luigi.Parameter()
    histogram = luigi.Parameter()

    def log(self):
        """
        defines output path for task logs in general log folder under ``branch_plot``
        """
        return f'{general["LogPath"]}/branch_plot/{self.year}/{self.region}/{self.systematic}/{self.histogram}.log'

    def requires(self):
        """
        task requires all histograms to be produced
        """
        return [AllHistoTasks(year=self.year)]

    def output(self):
        """
        tasks outputs a logfile and the plot in the plotfolder
        """
        return [law.LocalFileTarget(f'{general["PlotPath"]}/{self.year}/{self.region}/{self.systematic}/{self.histogram}.pdf'),
                law.LocalFileTarget(self.log())]

    def run(self):
        """
        tasks runs :mod:`python/plot_branch.py` and produces a logfile
        """
        self.save_execute(command=f'python python/plot_branch.py --year {self.year} --region {self.region} \
                                    --systematic {self.systematic} --histo {self.histogram}', log=self.log())



class AllBranchPlotTasks(law.WrapperTask):
    """
    A wrapper task to plot all histograms for all regions and systematic variations of a specific year

    :param year: year for which to produce the plots
    """
    year = luigi.Parameter()

    def requires(self):
        """
        defines required BranchPlotTasks
        """
        for histogram in histograms.keys():
            for region in regions.keys():
                for systematic in systematics.keys():
                    if systematics[systematic]['type'] == 'shape' and self.year in systematics[systematic]['years']:
                        if systematic == 'nominal':
                            yield BranchPlotTask(year=self.year, region=region, systematic=systematic, histogram=histogram)
                        else:
                            yield BranchPlotTask(year=self.year, region=region, systematic=systematic + 'UP', histogram=histogram)
                            yield BranchPlotTask(year=self.year, region=region, systematic=systematic + 'DOWN', histogram=histogram)
