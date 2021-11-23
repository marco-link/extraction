#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Defines some general helper functions
"""

from config.samples import samples
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



def get_event_weigths(year, sample, systematic):
    """
    generates weightstring from sample and systematic name

    :param year: year
    :param sample: sample name
    :param systematic: systematic sting (name and variation direction)
    :returns: weightstring
    """
    weightstring = '1'

    if 'EventWeights' in samples[sample][year].keys():
        for weight in samples[sample][year]['EventWeights']:
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
