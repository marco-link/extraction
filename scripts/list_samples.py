#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Just a small tool to list the available samples in a root directory
'''

from grid_tools import get_all_sample_names

from argparse import ArgumentParser
parser = ArgumentParser('list available samples')
parser.add_argument('version', help='')
parser.add_argument('year', help='')
parser.add_argument('--base_path',
                    help='root path of the sample, e.g. \
root://cmsxrootd-kit.gridka.de//store/user/mlink/WbNanoAODTools',
                    default='root://cmsxrootd-kit.gridka.de//store/user/mlink/WbNanoAODTools')

args = parser.parse_args()


all = get_all_sample_names(args.version, args.year, basepath=args.base_path)[0]
for s in all:
    print(s)
