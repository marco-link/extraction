#!/usr/bin/python
# -*- coding: utf-8 -*-

from config.samples import samples
from config.systematics import systematics


def get_event_weigths(year, sample, systematic):
    weightstring = '1'

    if 'EventWeights' in samples[sample][year].keys():
        for weight in samples[sample][year]['EventWeights']:
            if not weight:
                continue
            else:
                weightstring += '*({})'.format(weight)



    sys_name = systematic.replace('UP', '').replace('DOWN', '')
    direction = systematic.replace(sys_name, '')
    if sys_name in systematics.keys():
        if 'EventWeights' in systematics[sys_name].keys():
            for weight in systematics[sys_name]['EventWeights'][direction]:
                if not weight:
                    continue
                else:
                    weightstring += '*({})'.format(weight)

    return weightstring
