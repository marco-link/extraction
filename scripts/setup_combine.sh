#!/bin/bash

ulimit -s unlimited

export SCRAM_ARCH=slc7_amd64_gcc700
export CMSSW_BASE=CMSSW_10_2_13

export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch/
source $VO_CMS_SW_DIR/cmsset_default.sh

mkdir -p env
cd env


if [ -r "${CMSSW_BASE}" ];
then
    echo "${CMSSW_BASE} environment found"
else
    cmsrel ${CMSSW_BASE}
fi

cd ${CMSSW_BASE}/src

if [ -r "HiggsAnalysis/CombinedLimit" ];
then
    echo "combine git repo found"
else
    git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
    cd HiggsAnalysis/CombinedLimit; git fetch origin; git checkout v8.2.0; cd -
fi


if [ -r "CombineHarvester" ];
then
    echo "CombineHarvester git repo found"
else
    git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester

    scram b -j 8
fi

cmsenv
cd ../../../

export PYTHONPATH=$(pwd):$PYTHONPATH
