# -*- coding: utf-8 -*-

import law
import luigi

from workflow.BaseTask import HTCondorBaseTask

from helpers import histopath, getGridpaths
from job_definition import createHistoFillJobBranches
from config.data import data
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
    parallel_jobs = 1000

    def create_branch_map(self):
        """
        creates branchmap with an entry for input file
        
        FIXME: this needs a check of consistency with getGridpaths and data and datasets
        """
        
        
        return createHistoFillJobBranches(self.year)

    def htcondor_bootstrap_file(self):
        """
        run environment setup script
        """
        return law.util.rel_path(__file__, '../scripts/setup_pyenv.sh')

    def log(self):
        """
        defines output path for task logs under the path from :func:`config.general.histopath`
        """
        return histopath(year=self.year,
                         region=self.branch_data[0],
                         dataset=self.branch_data[1],
                         systematic='',
                         number=self.branch_data[3]).replace('.root', '.log')

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
