#!/usr/bin/env python
# -*- coding: utf-8 -*-

from fill_histos import fillhistos
from job_definition import createHistoFillJobBranches, createHistoMergeJobBranches
from multiprocessing import Pool 
import datetime
import os 

def fillworker(b):
    fillhistos(year=b[4], region=b[0], dataset_key=b[1], process_systematics=b[2], number=b[3], verbose=False)
    

def mergeworker(b):
    command = 'hadd -f '+ b['target'] + ' ' + b['source']
    if 0 == os.system( command + ' > /dev/null 2>&1') :
        return b['target']
    else:
        raise RuntimeError('problem running '+ command)
    
def fillHistos(year = '2017'):

    alljobs = createHistoFillJobBranches(year)
    
    #exit()
    print('created',len(alljobs),'jobs')
    
    starttime = datetime.datetime.now()
    
    #for i in alljobs.keys():
        
    p = Pool()
    import tqdm # not in repo
    r = list(tqdm.tqdm(p.imap(fillworker, list(alljobs.values())), total=len(alljobs.keys())))
    
    print('full run took', datetime.datetime.now()-starttime)
    
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
    r = list(tqdm.tqdm(p.imap(mergeworker, list(alljobs.values())), total=len(alljobs.keys())))
    
    print('full histo merge took', datetime.datetime.now()-starttime)

#fillHistos('2017')
#exit()
mergeHistos('2017')