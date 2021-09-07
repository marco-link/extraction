# -*- coding: utf-8 -*-
"""
Derived luigi.Task to execute commands failsafe

"""
import os
import luigi
import subprocess



class BaseTask(luigi.Task):

    def save_execute(self, command, log):
        logdir = os.path.dirname(log)
        os.makedirs(logdir, exist_ok=True)

        try:
            subprocess.check_output(command + ' &>' + log + '.tmp', shell=True)
            subprocess.call('mv -f {log}.tmp {log}'.format(log=log), shell=True)
        except subprocess.CalledProcessError as e:
            print('\n\033[1;31mAttention, attention!\033[0;0m')
            print(e)
            print('\n\n')
