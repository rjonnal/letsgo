import letsgo as lg
import config as cfg
import pandas as pd
import sys,os

"""This script lists all of the available parameters (aggregated dependent
variables) available in a given recording."""

datasets = lg.get_all_datasets(cfg.data_root)

rows = []

# make a huge dataframe with dataset info (patient, task, session, trial, and all params)
count = 0
for ds in datasets:
    print(count,ds.dataset_location)
    d = ds.get_aggregated_params()
    rows.append(d)
    count+=1

df = pd.DataFrame(rows)

os.makedirs(cfg.summary_folder,exist_ok=True)
outfn = os.path.join(cfg.summary_folder,'summary.csv')

df.to_csv(outfn,index=False)
