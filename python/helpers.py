#!/usr/bin/python
# -*- coding: utf-8 -*-

from config.samples import samples
from config.systematics import systematics


def get_event_weigths(year, sample, systematic='nom'):
    weightstring = ''
    if 'EventWeights' in samples[sample][year].keys():
        for weight in samples[sample][year]['EventWeights']:
            if not weight:
                continue
            if not weightstring:
                weightstring += '({})'.format(weight)
            else:
                weightstring += '*({})'.format(weight)
    if systematic in systematics.keys():
        if 'EventWeights' in systematics[systematic].keys():
            for weight in systematics[systematic]['EventWeights']:
                if not weight:
                    continue
                if not weightstring:
                    weightstring += '({})'.format(weight)
                else:
                    weightstring += '*({})'.format(weight)

    return weightstring
