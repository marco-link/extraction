# -*- coding: utf-8 -*-

import os
import law
import luigi
import subprocess

law.contrib.load('htcondor')


class BaseTask(law.Task):
    """
    law.Task with functions to execute commands with subprocess and log them if needed.
    Used as base for all other tasks in this project.
    """

    def save_execute(self, command: str, log: str) -> None:
        """
        Executes a command and gives a warning message if there is an error.
        The output is piped into the given log path extended by ``.tmp``, which is removed after successful execution.
        If the log folder doesn't exist it is generated.

        :param command: command to execute
        :param log: path of the logfile
        """

        logdir = os.path.dirname(log)
        os.makedirs(logdir, exist_ok=True)

        try:
            subprocess.check_output(command + ' &>' + log + '.tmp', shell=True)
            subprocess.call('mv -f {log}.tmp {log}'.format(log=log), shell=True)
        except subprocess.CalledProcessError as e:
            print('\n\033[1;31mAttention, attention!\033[0;0m')
            print(e)
            print('\n\n')


    def execute(self, command: str) -> None:
        """
        Executes a command and gives a warning message if there is an error.

        :param command: command to execute
        """

        try:
            subprocess.check_output(command, shell=True)
        except subprocess.CalledProcessError as e:
            print('\n\033[1;31mAttention, attention!\033[0;0m')
            print(e)
            print('\n\n')



class HTCondorBaseTask(law.htcondor.HTCondorWorkflow, law.LocalWorkflow, BaseTask):
    """
    law.Task with functions to execute commands with subprocess and log them if needed.
    Used as base for all other tasks in this project.

    :param transfer_logs: transfer job logs
    :param max_runtime: maximum job runtime
    """
    transfer_logs = luigi.BoolParameter(default=False)
    max_runtime = law.DurationParameter(default=2.0, unit='h', significant=False,
                                        description='maximum job runtime, default unit is hours, default: 2')

    def htcondor_output_directory(self):
        # the directory where submission meta data should be stored
        return law.LocalDirectoryTarget('.')

    def htcondor_job_config(self, config, job_num, branches):
        # render_variables are rendered into all files sent with a job
        config.render_variables['analysis_path'] = os.getenv('ANALYSIS_PATH')
        # force to run on CC7, http://batchdocs.web.cern.ch/batchdocs/local/submit.html#os-choice
        #config.custom_content.append(("requirements", "(OpSysAndVer =?= \"CentOS7\")"))
        # maximum runtime
        config.custom_content.append(('+MaxRuntime', int(self.max_runtime * 3600)))
        # copy the entire environment
        config.custom_content.append(('getenv', 'true'))
        # transfer proxy
        config.custom_content.append(('use_x509userproxy', 'true'))
        config.custom_content.append(('x509userproxy', os.getenv('X509_USER_PROXY')))
        # the CERN htcondor setup requires a "log" config, but we can safely set it to /dev/null
        # if you are interested in the logs of the batch system itself, set a meaningful value here
        config.custom_content.append(('log', '/dev/null'))
        return config
