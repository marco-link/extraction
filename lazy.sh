
law index --verbose

# law run AllBranchPlotTasks --year 2016 --print-status -1
nice -n 5 law run AllBranchPlotTasks --year 2016 --workers 4 # --HistoTask-workflow local
