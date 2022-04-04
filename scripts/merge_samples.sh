#!/bin/bash

# script to merge the datasets from NanoAODTools output
# only works on ETP infrastructure (sorry -_o_-)


SAMPLEPATH="/storage/gridka-nrg/mlink/WbNanoAODTools/2022-03-25_v2"
OUTDIR="/ceph/mlink/WbNanoAODTools/2022-03-25_v2/"


mkdir -p $OUTDIR
for sample in $SAMPLEPATH/*
do
    sample=${sample//$SAMPLEPATH/}
    echo $sample

    if [ ! -f $OUTDIR/$sample.txt ];
    then
        python2 python/merge.py $sample $SAMPLEPATH/$sample $OUTDIR/$sample.root &> $OUTDIR/$sample.txt
    else
        echo "Already processed!"
    fi
done
