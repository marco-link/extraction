#!/bin/bash

# script to move the merged files to the grid
# only works on ETP infrastructure (sorry \_O_/)

# run before the script to remove old files
# gfal-rm -r "gsiftp://cmssrm-kit.gridka.de:2811//pnfs/gridka.de/cms/disk-only/store/user/mlink/WbNanoAODTools/2017/"


SAMPLEVERSION="2022-07-01_v6"

SAMPLEPATH="/ceph/mlink/WbNanoAODTools/$SAMPLEVERSION"
GRIDPATH="gsiftp://cmssrm-kit.gridka.de:2811//pnfs/gridka.de/cms/disk-only/store/user/mlink/WbNanoAODTools/mc/2017/"

gfal-mkdir $GRIDPATH
for f in $SAMPLEPATH/*
do
    echo $f
    gfal-copy -p -t 10800 -T 10800 $f $GRIDPATH
done
