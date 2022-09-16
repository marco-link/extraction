

from config.datasets import datasets, all_samples
from config.systematics import systematics
from config.data import data as realdatadict
from config.regions import regions

from helpers import histopath, getGridpaths
    
def createHistoFillJobBranches(year, realdata=True, onlyrealdata=False, return_merge_target=False):
    branches = []
    targets = []
    
    for region in regions.keys():
        # data
        if realdata:
            for dataset in realdatadict.keys():
                for i in range(len(getGridpaths(year=year,
                                                setname=realdatadict[dataset]['FileName']))):
                    branches.append([region, dataset, ['None'], i,year])
    
        if onlyrealdata:
            continue
        # MC
        for dataset in datasets.keys():
            # loop over single input files
            for i in range(len(getGridpaths(year=year,
                                            setname=datasets[dataset]['FileName']))):
                applysyst=[]
                for systematic in systematics.keys():
                    # is shape systematic and applied in this year
                    if systematics[systematic]['type'] == 'shape' and year in systematics[systematic]['years']:
                        # systematic is applied for this dataset
                        if 'datasets' not in systematics[systematic].keys() or dataset in systematics[systematic]['datasets']:
                            if systematic == 'nominal':
                                applysyst.append(systematic)
                            else:
                                applysyst.append(systematic + 'Up')
                                applysyst.append(systematic + 'Down')
                                
                branches.append([region, dataset, applysyst, i, year])
                
    return dict(enumerate(branches))

def createHistoMergeJobBranches(year, create_dirs=False):
    out = [] #target and source
    
    def _entry(y,r,d,s):
        t = histopath(year, region, dataset, s, create_dir=create_dirs)
        s = t.replace('.root', '_*.root')
        return {'target': t, 'source': s}
    
    for region in regions.keys():
        for dataset in realdatadict.keys():
            out.append(_entry(year, region, dataset, 'None'))
        for dataset in datasets.keys():
            for systematic in systematics.keys():
                if systematics[systematic]['type'] == 'shape' and year in systematics[systematic]['years']:
                    if systematic == 'nominal':
                        out.append(_entry(year, region, dataset, 'nominal'))
                    else:
                        out.append(_entry(year, region, dataset, systematic+'Up'))
                        out.append(_entry(year, region, dataset, systematic+'Down'))
             
    return dict(enumerate(out))
