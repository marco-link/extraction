#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Defines some general helper functions
"""

from config.datasets import datasets
from config.systematics import systematics


def getSystsplit(systematic):
    """
    splits sytematic string into naem and variation direction.

    :param systematic: systematic sting constisting of systematic name and variation (``UP`` or ``DOWN``)
    :returns: systematic name, variation direction
    """
    sys_name = systematic.replace('UP', '').replace('DOWN', '')
    direction = systematic.replace(sys_name, '')

    return sys_name, direction



def get_event_weigths(year, dataset, systematic):
    """
    generates weightstring from dataset and systematic name

    :param year: year
    :param dataset: dataset name
    :param systematic: systematic sting (name and variation direction)
    :returns: weightstring
    """
    weightstring = '1'

    if 'EventWeights' in datasets[dataset][year].keys():
        for weight in datasets[dataset][year]['EventWeights']:
            if not weight:
                continue
            else:
                weightstring += '*({})'.format(weight)



    sys_name, direction = getSystsplit(systematic)
    if sys_name in systematics.keys():
        if 'EventWeights' in systematics[sys_name].keys():
            for weight in systematics[sys_name]['EventWeights'][direction]:
                if not weight:
                    continue
                else:
                    weightstring += '*({})'.format(weight)

    return weightstring
