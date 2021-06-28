#!/bin/bash

ulimit -s unlimited

# export SCRAM_ARCH=slc7_amd64_gcc700
# export CMSSW_BASE=CMSSW_10_2_13
#
#
# export VO_CMS_SW_DIR=/cvmfs/cms.cern.ch/
# source $VO_CMS_SW_DIR/cmsset_default.sh
# source /cvmfs/cms.cern.ch/common/crab-setup.sh
#
# if [ -r "${CMSSW_BASE}" ];
# then
#     echo "${CMSSW_BASE} environment found"
# else
#     cmsrel ${CMSSW_BASE}
# fi
#
# cd ${CMSSW_BASE}/src
#
# if [ -r "HiggsAnalysis/CombinedLimit" ];
# then
#     echo "combine git repo found"
# else
#     git clone https://github.com/cms-analysis/HiggsAnalysis-CombinedLimit.git HiggsAnalysis/CombinedLimit
#     cd HiggsAnalysis/CombinedLimit; git fetch origin; git checkout v8.2.0; cd -
# fi
#
#
# if [ -r "CombineHarvester" ];
# then
#     echo "CombineHarvester git repo found"
# else
#     git clone https://github.com/cms-analysis/CombineHarvester.git CombineHarvester
# fi
#
# cmsenv
# scram b -j 10
# cd ../../


export PYTHONPATH=$(pwd):$PYTHONPATH

# Source ROOT working with python 3
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.22.00/x86_64-centos7-gcc48-opt/bin/thisroot.sh


pynvname="venv_extraction"

if [ -r ./${pynvname} ];
then
    source ./${pynvname}/bin/activate
else
    virtualenv -p python3 ./${pynvname}

    source ./${pynvname}/bin/activate

    pip install --upgrade pip
    pip install --upgrade --force-reinstall --no-cache pip-review numpy scipy matplotlib mplhep pandas uproot luigi pre-commit

    pre-commit install
fi
