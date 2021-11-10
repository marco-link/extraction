# -*- coding: utf-8 -*-
"""
A luigi task to fperform the NLL fits
"""
import luigi

from workflow.BaseTask import BaseTask
from workflow.CombineCardTask import CombineCardTask

from config.general import general
from config.samples import gen_json


class WorkspaceTask(BaseTask):
    index = luigi.IntParameter()
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()


    def log(self):
        return f'{general["FitPath"]}/{self.fitname}/{self.index}/workspace.log'

    def requires(self):
        return CombineCardTask(cardmask=self.cardmask.format(i=self.index),
                               cardoutput=f'{general["CardPath"]}/{self.fitname}/{self.index}.txt',
                               histogram=self.histogram)

    def output(self):
        return [luigi.LocalTarget(self.log().replace('.log', '.root')),
                luigi.LocalTarget(self.log())]

    def run(self):
        self.save_execute(command=f'env -i sh scripts/execute_combine.sh text2workspace.py \
                                    {general["CardPath"]}/{self.fitname}/{self.index}.txt \
                                    -o {self.log().replace(".log", ".root")} -m 125 --PO verbose', log=self.log())



class ToyTask(BaseTask):
    index = luigi.IntParameter()
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()


    def log(self):
        return f'{general["FitPath"]}/{self.fitname}/{self.index}/toy.log'

    def requires(self):
        return WorkspaceTask(index=self.index, fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask)

    def output(self):
        return [luigi.LocalTarget(f'{general["FitPath"]}/{self.fitname}/{self.index}/toy.root'),
                luigi.LocalTarget(self.log())]

    def run(self):
        self.save_execute(command=f'env -i sh scripts/execute_combine.sh \
                                    combine -M GenerateOnly -v 3  -m 125 -n _toy_{self.fitname}_{self.index} \
                                    --redefineSignalPOIs r --setParameters r=1 \
                                    --freezeParameters r \
                                    --saveToys --expectSignal 1 -t -1 \
                                    {general["FitPath"]}/{self.fitname}/{self.index}/workspace.root', log=self.log())
        self.execute(f'mv -v higgsCombine_toy_{self.fitname}_{self.index}.GenerateOnly.*.root \
                       {general["FitPath"]}/{self.fitname}/{self.index}/toy.root')



class FitTask(BaseTask):
    index = luigi.IntParameter()
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()


    def log(self):
        return f'{general["FitPath"]}/{self.fitname}/{self.index}/fit.log'

    def requires(self):
        return [WorkspaceTask(index=self.index, fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask),
                ToyTask(index=19, fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask)]

    def output(self):
        return [luigi.LocalTarget(f'{general["FitPath"]}/{self.fitname}/{self.index}/NLLfit.root'),
                luigi.LocalTarget(self.log())]

    def run(self):
        self.save_execute(command=f'env -i sh scripts/execute_combine.sh \
                                    combine -M MultiDimFit -m 125 -v 3 -n _fit_{self.fitname}_{self.index} \
                                    --toysFile {general["FitPath"]}/{self.fitname}/19/toy.root  -t -1 \
                                    --setParameters r=1 --freezeParameters r --redefineSignalPOIs r \
                                    --X-rtd REMOVE_CONSTANT_ZERO_POINT=1 --saveNLL \
                                    {general["FitPath"]}/{self.fitname}/{self.index}/workspace.root', log=self.log())
        self.execute(f'mv -v higgsCombine_fit_{self.fitname}_{self.index}.MultiDimFit.*.root \
                       {general["FitPath"]}/{self.fitname}/{self.index}/NLLfit.root')


class AllFitTasks(luigi.WrapperTask):
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()

    def requires(self):
        for index in gen_json.keys():
            yield FitTask(index=index, fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask)
