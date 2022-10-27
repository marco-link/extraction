#!/usr/bin/env python
# -*- coding: utf-8 -*-

from local_jobs import fillHistos, mergeHistos, plotHistos


fillHistos('2017')
mergeHistos('2017')
plotHistos('2017', signal='WbWbX_19')