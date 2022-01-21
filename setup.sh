#!/bin/bash

export ANALYSIS_PATH="$(pwd)"
export LAW_HOME="$ANALYSIS_PATH/.law"
export LAW_CONFIG_FILE="$ANALYSIS_PATH/law.cfg"
export PYTHONPATH=$ANALYSIS_PATH:$PYTHONPATH

# function to build documentation
buildDoc()
{
    cd doc
    sphinx-apidoc -f -o source ../workflow --tocfile workflow
    sphinx-apidoc -f -o source ../python --tocfile python_scripts
    make html
    cd -
}

env -i sh scripts/setup_combine.sh
source scripts/setup_pyenv.sh
