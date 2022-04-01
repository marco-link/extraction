
voms-proxy-info

if [ $? -eq 0 ]
then
    # setup proxy
    cp -v `voms-proxy-info -path` $HOME/x509up
    export X509_USER_PROXY=$HOME/x509up

    law index --verbose
    # law run AnalysisTask --print-status -1
    nice -n 5 law run AnalysisTask --workers 4 # --HistoTask-workflow local
else
    echo "============================================="
    echo " Please setup a proxy first!"
    echo " It is required to access data from the GRID"
    echo "============================================="
fi
