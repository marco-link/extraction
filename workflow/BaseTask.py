# -*- coding: utf-8 -*-
"""
Derived luigi.Task to run task based on timestamps

found in http://stackoverflow.com/a/29304506
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


    def complete(self):
        def to_list(obj):
            if type(obj) in (type(()), type([])):
                return obj
            else:
                return [obj]

        def mtime(path):
            return os.path.getmtime(path)

        if not all(os.path.exists(out.path) for out in to_list(self.output())):
            return False

        self_mtime = min(mtime(out.path) for out in to_list(self.output()))

        # the below assumes a list of requirements, each with a list of outputs. YMMV
        for el in to_list(self.requires()):
            if not el.complete():
                return False
            for output in to_list(el.output()):
                if mtime(output.path) > self_mtime:
                    return False

        return True
