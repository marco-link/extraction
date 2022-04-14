# -*- coding: utf-8 -*-

import law
import luigi

from workflow.BranchPlotTask import AllBranchPlotTasks
from workflow.NLLPlotTask import NLLPlotTask

from config.general import allyears, lumi
from config.regions import regions


class AnalysisTask(law.WrapperTask):
    """
    A wrapper task task to run the full analysis

    :param NLLoptions: option to give to the NLL plotting script
    """
    NLLoptions = luigi.Parameter(default='--ymax 30 ')

    def requires(self):
        """
        defines required analysis tasks
        """
        yield NLLPlotTask(fitname='all',
                          histogram='fitcategories',
                          cardmask='/*/*/fitcategories.txt',
                          options=self.NLLoptions + f' --lumi {lumi["total"]}')

        # years
        for year in allyears:
            yield AllBranchPlotTasks(year=year)
            yield NLLPlotTask(fitname=year,
                              histogram='fitcategories',
                              cardmask='/' + year + '/*/fitcategories.txt',
                              options=self.NLLoptions + f' --lumi {lumi[year]}')

        # regions
        for region in regions.keys():
            yield NLLPlotTask(fitname=region,
                              histogram='fitcategories',
                              cardmask='/*/' + region + '/fitcategories.txt',
                              options=self.NLLoptions + f' --lumi {lumi["total"]}')
