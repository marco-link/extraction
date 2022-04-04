#!/bin/bash

# script to move the merged files to the grid
# only works on ETP infrastructure (sorry \_O_/)


SAMPLEPATH="/ceph/mlink/WbNanoAODTools/2022-04-01_v3"
GRIDPATH="gsiftp://cmssrm-kit.gridka.de:2811//pnfs/gridka.de/cms/disk-only/store/user/mlink/WbNanoAODTools/2017/"

gfal-mkdir $GRIDPATH
for f in $SAMPLEPATH/*
do
    echo $f
    gfal-copy --timeout 7200 $f $GRIDPATH
done
