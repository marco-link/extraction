#!/bin/bash

echo $@

source scripts/setup_combine.sh
combineCards.py $1 > $2
