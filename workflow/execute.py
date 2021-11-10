# -*- coding: utf-8 -*-

import luigi

from workflow.BranchPlotTask import AllBranchPlotTasks
from workflow.FitTask import AllFitTasks

from config.general import allyears
from config.regions import regions


if __name__ == '__main__':
    tasks = []

    # all combined
    tasks.append(AllFitTasks(fitname='all', histogram='binCategory', cardmask='cards/*/*/binCategory_WbWbX_{i}.txt'))

    # regions
    for region in regions.keys():
        tasks.append(AllFitTasks(fitname=region, histogram='binCategory', cardmask='cards/*/' + region + '/binCategory_WbWbX_{i}.txt'))

    # years
    for year in allyears:
        tasks.append(AllFitTasks(fitname=year, histogram='binCategory', cardmask='cards/' + year + '/*/binCategory_WbWbX_{i}.txt'))
        tasks.append(AllBranchPlotTasks(year=year))

    luigi.build(tasks, workers=32, local_scheduler=True, log_level='INFO')
