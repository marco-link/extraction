#!/bin/bash

# script to merge the datasets from NanoAODTools output
# only works on ETP infrastructure (sorry \_O_/)


SAMPLEVERSION="2022-04-20_v4"

SAMPLEPATH="/storage/gridka-nrg/mlink/WbNanoAODTools/$SAMPLEVERSION/2017"
OUTDIR="/ceph/mlink/WbNanoAODTools/$SAMPLEVERSION/"


mkdir -p $OUTDIR
for sample in $SAMPLEPATH/*
do
    sample=${sample//$SAMPLEPATH/}
    echo $sample

    for shard in $SAMPLEPATH/$sample/*/*/*
    do
        echo $(basename $shard)
        logfile=$OUTDIR/${sample}_$(basename $shard).txt

        if [ ! -f $logfile ];
        then
            python2 -u python/merge.py ${sample} $shard $OUTDIR/${sample}_$(basename $shard).root &> $logfile
        else
            echo "Already processed!"
        fi
    done
done
