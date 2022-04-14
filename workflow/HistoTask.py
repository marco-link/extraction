# -*- coding: utf-8 -*-

import law
import luigi

from workflow.BaseTask import HTCondorBaseTask

from config.general import histopath, getGridpaths
from config.datasets import datasets
from config.regions import regions
from config.systematics import systematics


class HistoTask(HTCondorBaseTask):
    """
    A luigi task to produce histograms

    :param year: year for which to produce the histograms
    :param region: region for which to produce the histograms
    """
    year = luigi.Parameter()
    max_runtime = 8 #hours

    def create_branch_map(self):
        """
        creates branchmap with an entry for input file
        """
        branches = []
        for region in regions.keys():
            for dataset in datasets.keys():
                for systematic in systematics.keys():
                    # is shape systematic and applied in this year
                    if systematics[systematic]['type'] == 'shape' and self.year in systematics[systematic]['years']:
                        # systematic is applied for this dataset
                        if 'datasets' not in systematics[systematic].keys() or dataset in systematics[systematic]['datasets']:
                            # loop over single input files
                            for i in range(len(getGridpaths(isMC=datasets[dataset]['MC'],
                                                            year=self.year,
                                                            filename=datasets[dataset]['FileName']))):
                                if systematic == 'nominal':
                                    branches.append([region, dataset, systematic, i])
                                else:
                                    branches.append([region, dataset, systematic + 'UP', i])
                                    branches.append([region, dataset, systematic + 'DOWN', i])

        return dict(enumerate(branches))

    def htcondor_bootstrap_file(self):
        """
        run environment setup script
        """
        return law.util.rel_path(__file__, '../scripts/setup_pyenv.sh')

    def log(self):
        """
        defines output path for task logs under the path from :func:`config.general.histopath`
        """
        return histopath(isMC=datasets[self.dataset]['MC'],
                         year=self.year,
                         filename=self.dataset,
                         region=self.branch_data[0],
                         systematic=self.branch_data[1],
                         number=self.branch_data[2]).replace('.root', '.log')

    def output(self):
        """
        tasks outputs a logfile and a root file inside the path from :func:`config.general.histopath`, containing the histogram
        """
        return [law.LocalFileTarget(self.log()),
                law.LocalFileTarget(self.log().replace('.log', '.root'))]

    def run(self):
        """
        tasks runs :mod:`python/fill_histos.py` and produces a logfile
        """
        self.save_execute(command=f'python -u python/fill_histos.py --year {self.year} \
                                                                    --region {self.branch_data[0]} \
                                                                    --dataset {self.branch_data[1]} \
                                                                    --systematic {self.branch_data[2]} \
                                                                    --number {self.branch_data[3]}', log=self.log())



class AllHistoTasks(law.WrapperTask):
    """
    A wrapper task task to produce all histograms of a year

    :param year: year for which to produce the histograms
    """
    year = luigi.Parameter()

    def requires(self):
        """
        defines required HistoTasks
        """
        for dataset in datasets.keys():
            yield HistoTask(year=self.year)
