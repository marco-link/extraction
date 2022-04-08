#!/bin/bash

# script to merge the datasets from NanoAODTools output
# only works on ETP infrastructure (sorry \_O_/)

GRIDPATH="root://cmsxrootd-kit.gridka.de//store/user/mlink/WbNanoAODTools/2022-04-01_v3"
SAMPLEPATH="/storage/gridka-nrg/mlink/WbNanoAODTools/2022-04-01_v3"
OUTDIR="./config/mc/2017/"

mkdir -p $OUTDIR
for sample in $SAMPLEPATH/*
do
    dataset=${sample//$SAMPLEPATH/}
    echo $dataset

    ls -1 $sample/**/*.root > $OUTDIR/$dataset.txt
    sed -i "s!${SAMPLEPATH}!${GRIDPATH}!g" $OUTDIR/$dataset.txt
done
