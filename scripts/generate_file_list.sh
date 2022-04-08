#!/bin/bash

# script to merge the datasets from NanoAODTools output
# only works on ETP infrastructure (sorry \_O_/)

GRIDPATH="root://cmsxrootd-kit.gridka.de//store/user/mlink/WbNanoAODTools/2022-04-01_v3/"
SAMPLEPATH="/storage/gridka-nrg/mlink/WbNanoAODTools/2022-04-01_v3"
OUTDIR="./config/mc/2017/"

mkdir -p $OUTDIR
for sample in $SAMPLEPATH/*
do
    sample=${sample//$SAMPLEPATH/}
    echo $sample

    ls -1 $SAMPLEPATH/$sample/**/*.root > $OUTDIR/$sample.txt
    sed -i "s!${SAMPLEPATH}!${GRIDPATH}!g" $OUTDIR/$sample.txt
#
#     if [ ! -f $OUTDIR/$sample.txt ];
#     then
#         python2 -u python/merge.py $sample $SAMPLEPATH/$sample $OUTDIR/$sample.root &> $OUTDIR/$sample.txt
#     else
#         echo "Already processed!"
#     fi
done
