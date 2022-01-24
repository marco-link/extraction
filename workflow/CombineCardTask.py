# -*- coding: utf-8 -*-
import os
import glob
import law
import luigi


from workflow.BaseTask import BaseTask
from workflow.DatacardTask import AllDatacardTasks

from config.general import general, allyears


class CombineCardTask(BaseTask):
    """
    A wrapper task to combine datacards from different years/regions

    :param cardmask: cardmask to select specific cards e.g. ``cards/<year or *>/<region or *>/<histogram>.txt``.
    :param cardoutput: output path for the combined card
    :param histogram: histogram to used for card production
    """
    cardmask = luigi.Parameter()
    cardoutput = luigi.Parameter()
    histogram = luigi.Parameter()


    def log(self):
        """
        defines output path for task logs in general log folder under ``combineCards``
        """
        return f'{general["LogPath"]}/combineCards/{self.cardoutput}.log'

    def requires(self):
        """
        task requires the datacards for all years to be produced
        """
        return [AllDatacardTasks(year=y, histogram=self.histogram) for y in allyears]

    def output(self):
        """
        tasks outputs a logfile and the combined card
        """
        return [law.LocalFileTarget(self.cardoutput),
                law.LocalFileTarget(self.log())]

    def run(self):
        """
        tasks runs ``scripts/combineCards.sh`` script to combine cards and produces a logfile
        """
        os.makedirs(os.path.dirname(self.cardoutput), exist_ok=True)
        files = ' '.join([f'.={f}' for f in glob.glob(general['CardPath'] + self.cardmask, recursive=True)])
        self.save_execute(command=f'env -i sh scripts/combineCards.sh "{files}" {self.cardoutput}', log=self.log())
