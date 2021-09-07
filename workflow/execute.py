# -*- coding: utf-8 -*-

import luigi

from workflow.BranchPlotTask import AllBranchPlotTasks
from workflow.DatacardTask import AllDatacardTasks



years = [
    '2016',
    #'2017',
    #'2018',
]


if __name__ == '__main__':
    tasks = []

    for year in years:
        tasks.append(AllBranchPlotTasks(year=year))
        tasks.append(AllDatacardTasks(year=year, histogram='Reco_Wb'))

    luigi.build(tasks, workers=32, local_scheduler=True, log_level='INFO')
