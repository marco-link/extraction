# -*- coding: utf-8 -*-

import luigi
import law

from workflow.BaseTask import HTCondorBaseTask

from config.general import histopath
from config.samples import samples
from config.regions import regions
from config.systematics import systematics


class HistoTask(HTCondorBaseTask):
    """
    A luigi task to produce histograms

    :param year: year for which to produce the histograms
    :param region: region for which to produce the histograms
    """
    year = luigi.Parameter()
    region = luigi.Parameter()

    def create_branch_map(self):
        """
        creates branchmap with an entry for each applied systematic
        """
        branches = []
        for sample in samples.keys():
            for systematic in systematics.keys():
                # is shape systematic and applied in this year
                if systematics[systematic]['type'] == 'shape' and self.year in systematics[systematic]['years']:
                    # systematic is applied for this sample
                    if 'samples' not in systematics[systematic].keys() or sample in systematics[systematic]['samples']:
                        if systematic == 'nominal':
                            branches.append([sample, systematic])
                        else:
                            branches.append([sample, systematic + 'UP'])
                            branches.append([sample, systematic + 'DOWN'])

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
        return histopath(isMC=samples[self.branch_data[0]]['MC'],
                         year=self.year,
                         filename=self.branch_data[0],
                         region=self.region,
                         systematic=self.branch_data[1]).replace('.root', '.log')

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
        self.save_execute(command=f'python python/fill_histos.py --year {self.year} --sample {self.branch_data[0]} \
                                    --region {self.region} --systematic {self.branch_data[1]}', log=self.log())



class AllHistoTasks(law.WrapperTask):
    """
    A luigi wrapper task to produce all histograms of a year

    :param year: year for which to produce the histograms
    """
    year = luigi.Parameter()

    def requires(self):
        """
        defines required HistoTasks
        """
        for region in regions.keys():
            yield HistoTask(year=self.year, region=region)
