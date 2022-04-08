#!/bin/bash

# script to merge the datasets from NanoAODTools output
# only works on ETP infrastructure (sorry \_O_/)


SAMPLEPATH="/storage/gridka-nrg/mlink/WbNanoAODTools/2022-04-01_v3"
OUTDIR="/ceph/mlink/WbNanoAODTools/2022-04-01_v3/"


mkdir -p $OUTDIR
for sample in $SAMPLEPATH/*
do
    sample=${sample//$SAMPLEPATH/}
    echo $sample

    if [ ! -f $OUTDIR/$sample.txt ];
    then
        python2 -u python/merge.py $sample $SAMPLEPATH/$sample $OUTDIR/$sample.root &> $OUTDIR/$sample.txt
    else
        echo "Already processed!"
    fi
done
