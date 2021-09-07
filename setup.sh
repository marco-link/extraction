#!/bin/bash

pynvname="venv_extraction"

# make sure combine environment is setup
env -i sh scripts/setup_combine.sh

# Source ROOT working with python 3
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.24.06/x86_64-centos7-gcc48-opt/bin/thisroot.sh


cd env

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

cd -
export PYTHONPATH=$(pwd):$PYTHONPATH
