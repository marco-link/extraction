#!/bin/bash

pynvname="extraction"

# Source ROOT working with python 3
source /cvmfs/sft.cern.ch/lcg/app/releases/ROOT/6.24.06/x86_64-centos7-gcc48-opt/bin/thisroot.sh

cd $ANALYSIS_PATH

if [ -r ./env/${pynvname} ];
then
    source ./env/${pynvname}/bin/activate
else
    cd env
    virtualenv -p python3 ./${pynvname}
    cd -

    source ./env/${pynvname}/bin/activate

    pip install --upgrade --no-cache-dir pip
    pip install --no-cache-dir pre-commit sphinx sphinx-rtd-theme sphinx-autodoc-typehints \
                               numpy scipy matplotlib pandas mplhep uproot awkward \
                               luigi==2.8.13 law==0.1.6

    pre-commit install
fi
