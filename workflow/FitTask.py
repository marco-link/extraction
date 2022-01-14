# -*- coding: utf-8 -*-

import luigi

from workflow.BaseTask import BaseTask
from workflow.CombineCardTask import CombineCardTask

from config.general import general


#TODO update documentation



class WorkspaceTask(BaseTask):
    """
    A luigi task to produce the workspace required for the fit

    :param fitname: unique name of the fit
    :param histogram: histogram for which to produce the workspace
    :param cardmask: cardmask to select specific cards e.g. ``cards/<year or *>/<region or *>/<histogram>_{i}.txt``.
    """
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()


    def log(self):
        """
        defines output path for task logs in the fit folder named ``workspace.log``
        """
        return f'{general["FitPath"]}/{self.fitname}/workspace.log'

    def requires(self):
        """
        task requires the combined cards to be produced
        """
        return [CombineCardTask(cardmask=self.cardmask,
                                cardoutput=f'{general["CardPath"]}/{self.fitname}.txt',
                                histogram=self.histogram)]

    def output(self):
        """
        tasks outputs a logfile and the workspace inside the fit folder named ``workspace.root``
        """
        return [luigi.LocalTarget(self.log().replace('.log', '.root')),
                luigi.LocalTarget(self.log())]

    def run(self):
        """
        tasks runs ``text2workspace.py`` in combine envirnoment and produces a logfile
        """
        self.save_execute(command=f'env -i sh scripts/execute_combine.sh text2workspace.py \
                                    {general["CardPath"]}/{self.fitname}.txt \
                                    -P HiggsAnalysis.CombinedLimit.WbWbXModel:DefaultWbWbXModel \
                                    -o {self.log().replace(".log", ".root")}', log=self.log())



class ToyTask(BaseTask):
    """
    A luigi task to produce the toy required for the fit

    :param fitname: unique name of the fit
    :param histogram: histogram for which to produce the toy
    :param cardmask: cardmask to select specific cards e.g. ``cards/<year or *>/<region or *>/<histogram>_{i}.txt``.
    """
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()
    parameters = luigi.Parameter(default='r=1,r,m_top=172.5,gamma_t=1.322') # SM values

    def log(self):
        """
        defines output path for task logs in gthe fit folder named ``toy.log``
        """
        return f'{general["FitPath"]}/{self.fitname}/toy.log'

    def requires(self):
        """
        task requires the workspace to be produced
        """
        return [WorkspaceTask(fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask)]

    def output(self):
        """
        tasks outputs a logfile and the toy inside the fit folder named ``toy.root``
        """
        return [luigi.LocalTarget(f'{general["FitPath"]}/{self.fitname}/toy.root'),
                luigi.LocalTarget(self.log())]

    def run(self):
        """
        tasks runs ``combine -M GenerateOnly`` in combine envirnoment and produces a logfile
        """
        self.save_execute(command=f'env -i sh scripts/execute_combine.sh \
                                    combine -M GenerateOnly -v 3 -n _toy_{self.fitname} \
                                    --redefineSignalPOIs r,m_top,gamma_t --setParameters {self.parameters} \
                                    --freezeParameters r,m_top,gamma_t \
                                    --saveToys -t -1 \
                                    {general["FitPath"]}/{self.fitname}/workspace.root', log=self.log())
        self.execute(f'mv -v higgsCombine_toy_{self.fitname}.GenerateOnly.*.root \
                       {general["FitPath"]}/{self.fitname}/toy.root')



class FitTask(BaseTask):
    """
    A luigi task to produce fit the NLL

    :param fitname: unique name of the fit
    :param histogram: histogram for which to produce the workspace
    :param cardmask: cardmask to select specific cards e.g. ``cards/<year or *>/<region or *>/<histogram>_{i}.txt``.
    TODO
    """
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()
    profiled = luigi.BoolParameter(default=False)
    points = luigi.IntParameter(default=1000)


    def log(self):
        """
        defines output path for task logs in gthe fit folder named ``fit.log``
        """
        if self.profiled:
            return f'{general["FitPath"]}/{self.fitname}/fit_profiled.log'
        else:
            return f'{general["FitPath"]}/{self.fitname}/fit.log'

    def requires(self):
        """
        task requires the workspace and the SM toy to be produced
        """
        return [WorkspaceTask(fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask),
                ToyTask(fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask)]

    def output(self):
        """
        tasks outputs a logfile and the NLL fit inside the fit folder named ``fit.root`` or ``fit_profiled.root``
        """
        if self.profiled:
            return [luigi.LocalTarget(f'{general["FitPath"]}/{self.fitname}/fit_profiled.root'),
                    luigi.LocalTarget(self.log())]
        else:
            return [luigi.LocalTarget(f'{general["FitPath"]}/{self.fitname}/fit.root'),
                    luigi.LocalTarget(self.log())]

    def run(self):
        """
        tasks runs ``combine -M MultiDimFit`` in combine environment and produces a logfile
        """
        ranges = 'gamma_t=0.5,10.0'
        pois = 'gamma_t'
        if not self.profiled:
            ranges += ':m_top=171.5,173.5'
            pois += ',m_top'

        self.save_execute(command=f'env -i sh scripts/execute_combine.sh \
                                    combineTool.py -M MultiDimFit -v 3 -n _fit_{self.fitname}_{self.profiled} \
                                    --algo grid --alignEdges 1 --points {self.points} \
                                    --toysFile {general["FitPath"]}/{self.fitname}/toy.root  -t -1 \
                                    --redefineSignalPOIs {pois} \
                                    --setParameters r=1,m_top=175.2,gamma_t=1.322 \
                                    --freezeParameters r --floatOtherPOIs 1 \
                                    --setParameterRanges {ranges} \
                                    {general["FitPath"]}/{self.fitname}/workspace.root', log=self.log())
        if self.profiled:
            self.execute(f'mv -v higgsCombine_fit_{self.fitname}_{self.profiled}.MultiDimFit.*.root \
                        {general["FitPath"]}/{self.fitname}/fit_profiled.root')
        else:
            self.execute(f'mv -v higgsCombine_fit_{self.fitname}_{self.profiled}.MultiDimFit.*.root \
                        {general["FitPath"]}/{self.fitname}/fit.root')



class AllFitTasks(luigi.WrapperTask):
    """
    A luigi wrapper task handle all fit related tasks from workspace and toy generation to the final fit.

    :param fitname: unique name of the fit
    :param histogram: histogram for which to produce the workspace
    :param cardmask: cardmask to select specific cards e.g. ``cards/<year or *>/<region or *>/<histogram>_{i}.txt``.
    """
    fitname = luigi.Parameter()
    histogram = luigi.Parameter()
    cardmask = luigi.Parameter()

    def requires(self):
        """
        defines required FitTasks
        """
        yield FitTask(fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask, profiled=False)
        yield FitTask(fitname=self.fitname, histogram=self.histogram, cardmask=self.cardmask, profiled=True)
