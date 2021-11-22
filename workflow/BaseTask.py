# -*- coding: utf-8 -*-

import os
import luigi
import subprocess



class BaseTask(luigi.Task):
    """
    luigi.Task with functions to execute commands with subprocess and log them if needed.
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
