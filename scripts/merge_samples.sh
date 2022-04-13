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
