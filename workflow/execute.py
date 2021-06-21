# -*- coding: utf-8 -*-

import luigi

from workflow.BranchPlotTask import AllBranchPlotTasks

#from config.samples import samples
#from config.regions import regions
#from config.systematics import systematics
#from config.histograms import histograms

years = [
    2016,
    #2017,
    #2018,
]


if __name__ == '__main__':
    tasks = []

    for year in years:
        tasks.append(AllBranchPlotTasks(year=year))

    luigi.build(tasks, workers=20, local_scheduler=True, log_level='INFO')
