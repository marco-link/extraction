#!/bin/bash

# script to merge the datasets from NanoAODTools output
# only works on ETP infrastructure (sorry \_O_/)

GRIDPATH="root://cmsxrootd-kit.gridka.de//store/user/mlink/WbNanoAODTools/2017"
SAMPLEPATH="/storage/gridka-nrg/mlink/WbNanoAODTools/2017"

OUTDIR="./config/mc/2017/"

rm -r $OUTDIR
mkdir -p $OUTDIR
for sample in $SAMPLEPATH/*.root
do
    dataset=$(basename $sample)
    dataset=${dataset::-10}
    echo $dataset

    echo ${sample//$SAMPLEPATH/$GRIDPATH} >> $OUTDIR/$dataset.txt
done
