#!/bin/bash

echo $@

source scripts/setup_combine.sh
python2 python/build_cards.py $@
