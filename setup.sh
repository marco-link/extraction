#!/bin/bash

export PYTHONPATH=$(pwd):$PYTHONPATH

# Source ROOT working with python 3
# source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.22.00/x86_64-centos7-gcc48-opt/bin/thisroot.sh

source /work/mlink/myroot/bin/thisroot.sh

pynvname="venv_extraction"

if [ -r ./${pynvname} ];
then
    source ./${pynvname}/bin/activate
else
    virtualenv -p python3 ./${pynvname}

    source ./${pynvname}/bin/activate

    pip install --upgrade pip
    pip install --upgrade --force-reinstall --no-cache numpy scipy matplotlib mplhep pandas uproot luigi pre-commit

    pre-commit install
fi
