

from fill_histos import fillhistos
from plot_branch import plot
from job_definition import createHistoFillJobBranches, createHistoMergeJobBranches, createHistoPlotJobBranches
from multiprocessing import Pool 
import datetime
import os 

def _fillHistosWorker(b):
    fillhistos(year=b[4], region=b[0], dataset_key=b[1], process_systematics=b[2], number=b[3], verbose=False)
    
def fillHistos(year):

    alljobs = createHistoFillJobBranches(year)
    
    #exit()
    print('created',len(alljobs),'jobs')
    
    starttime = datetime.datetime.now()
    
    #for i in alljobs.keys():
        
    p = Pool()
    import tqdm # not in repo
    r = list(tqdm.tqdm(p.imap(_fillHistosWorker, list(alljobs.values())), total=len(alljobs.keys())))
    
    print('full run took', datetime.datetime.now()-starttime)
    

def _mergeHistosWorker(b):
    command = 'hadd -f '+ b['target'] + ' ' + b['source']
    if 0 == os.system( command + ' > /dev/null 2>&1') :
        return b['target']
    else:
        raise RuntimeError('problem running '+ command)
        
def mergeHistos(year):
    starttime = datetime.datetime.now()
    
    print('creating histo merge rules...')
    alljobs = createHistoMergeJobBranches(year, create_dirs=False)#dirs were created with fill histos
    #print(alljobs)
    #exit()
    #exit()
    print('merge histos...')
    p = Pool()
    import tqdm # not in repo
    r = list(tqdm.tqdm(p.imap(_mergeHistosWorker, list(alljobs.values())), total=len(alljobs.keys())))
    
    print('full histo merge took', datetime.datetime.now()-starttime)


def _plotHistosWorker(b):
    plot(b['year'], b['region'], b['syst'], b['histo'], b['signal'])

def plotHistos(year, signal):
    starttime = datetime.datetime.now()
    alljobs = createHistoPlotJobBranches(year, signal)
    print('created',len(alljobs),'jobs')
    p = Pool(1)
    import tqdm # not in repo
    r = list(tqdm.tqdm(p.imap(_plotHistosWorker, alljobs), total=len(alljobs)))
    
    print('full run took', datetime.datetime.now()-starttime)