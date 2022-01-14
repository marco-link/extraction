# -*- coding: utf-8 -*-

"""
main file run the `luigi <https://luigi.readthedocs.io/en/stable/>`_ workflow.
Tasks, number of workers and plotoptions can be modified.
"""

import luigi

from workflow.BranchPlotTask import AllBranchPlotTasks
from workflow.NLLPlotTask import NLLPlotTask

from config.general import allyears, lumi
from config.regions import regions


NLLoptions = '--ymax 30 '


if __name__ == '__main__':
    tasks = []

    # all combined
    tasks.append(NLLPlotTask(fitname='all', histogram='binCategory',
                             cardmask='cards/*/*/binCategory.txt',
                             options=NLLoptions + f' --lumi {lumi["total"]}'))

    # regions
    for region in regions.keys():
        tasks.append(NLLPlotTask(fitname=region, histogram='binCategory',
                                 cardmask='cards/*/' + region + '/binCategory.txt',
                                 options=NLLoptions + f' --lumi {lumi["total"]}'))

    # years
    for year in allyears:
        tasks.append(AllBranchPlotTasks(year=year))
        tasks.append(NLLPlotTask(fitname=year, histogram='binCategory',
                                 cardmask='cards/' + year + '/*/binCategory.txt',
                                 options=NLLoptions + f' --lumi {lumi[year]}'))


    luigi.build(tasks, workers=32, local_scheduler=True, log_level='INFO')
