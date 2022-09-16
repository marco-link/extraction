'''

gfal-based sample file listing tools.
Transparently uses system calls if the path is not on the grid (much faster)

Installing the official gfal tools into the virtual environment did not work easily.
However, we only need some simple parts of it here, so this file contains some wrappers
to make them accessible via python in an easy way.

'''

import subprocess
import os

#just for convenience
def _syscall(s):
    
    res = subprocess.check_output(s, shell=True)
    return res


def gfal_ls(path: str):
    
    path = path.strip()
    if path[:7] != 'root://': #not grid, use posix call
        return os.listdir(path)
    
    #the PATH unset is necessary for >sl6 machines. Otherwise the venv causes an error
    r = str(_syscall("PATH=/usr/local/bin:/usr/bin:/usr/local/sbin:/usr/sbin gfal-ls "+path), 'utf-8')
    r = r.split('\n')
    r = [e for e in r if e != ''] #remove empty
    return r


def get_all_sample_files(root_path):
    
    '''
    Since the gfal-ls call is slow, this assumes the standard sample format of:
    root_path/<some numbers>/XXXX/<files here>.root
    '''
    
    allpaths = []
    
    subdirs = gfal_ls(root_path)
    for sd in subdirs:
        ssdirs = gfal_ls(root_path+'/'+sd)
        for ssd in ssdirs:
            files = gfal_ls(root_path+'/'+sd+'/'+ssd)
            for f in files:
                if len(f)>5 and f[-5:] == '.root':
                    allpaths.append(root_path+'/'+sd+'/'+ssd+'/'+f)
                    
    return allpaths


def get_all_sample_names(version, year=2017, basepath="root://cmsxrootd-kit.gridka.de//store/user/mlink/WbNanoAODTools"):
    
    '''
    Returns a list of available sample names (e.g. DYJetsToLL_M-50_TuneCP5_13TeV-amcatnloFXFX-pythia8) 
    and also the full path to prepend to it (e.g. root://cmsxrootd....)
    '''
    
    year = str(year)
    fullpath = basepath+'/'+version+'/'+year
    samples = gfal_ls(basepath+'/'+version+'/'+year)
    return samples, fullpath
    
  
    
    
    