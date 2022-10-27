#!/bin/bash

source scripts/setup_analysisenv.sh
env -i sh scripts/setup_combine.sh
source scripts/setup_pyenv.sh
export PATH=`pwd`/scripts/:$PATH
export PYTHONPATH=`pwd`/python:$PYTHONPATH
