import letsgo as lg
import glob,os,sys
from pathlib import Path
import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

data_root = '/home/rjonnal/Dropbox/Data/eye_tracking_working/'

# recursively identify all non_aggregated files
p = Path(data_root)
na_files = p.rglob('*drift_non_aggregated.csv')

na_files = [str(f) for f in na_files if str(f).find('Fixation_30s_PF')>-1]

subjects = ['NeuroSleep_011','NeuroSleep_019','NeuroSleep_022','NeuroSleep_013','NeuroSleep_021','NeuroSleep_026']


for f in na_files:
    f = str(f)
    for condition in ['WR','SD']:
        for subject in subjects:
            
            if f.find(condition)>-1:
                print(f)
