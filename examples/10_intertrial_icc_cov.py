import letsgo as lg
import config as cfg
import pandas as pd
import numpy as np
import sys,os

"""This script gets all of the available parameters (aggregated dependent
variables) from a set of recordings (everything located below cfg.data_root),
and stores them all in a single CSV file, if necessary, and then illustrates
how to use pandas to calculate ICC and COV for trials within the same session."""

summary_df_fn = os.path.join(cfg.summary_folder,'summary.csv')

try:
    df = pd.read_csv(summary_df_fn)
except FileNotFoundError:
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

    df.to_csv(outfn,index=False)


# get the columns of df that are numerical
params = []
for col in df.columns:
    dtype = df[col].dtype
    if dtype in ['float64','int64']:
        params.append(col)
        
tasks = df['task'].unique()
patient_codes = df['patient_code'].unique()
conditions = df['condition'].unique()
sessions = df['session'].unique()

# iterate through all subject/session/condition/task combinations
# to see which ones have a minimum of 2 trials
for task in tasks:
    for condition in conditions:
        # calculate ICCs separately for each task-condition combination
        counter = {}
        icc_df = []
        for patient_code in patient_codes:
            for session in sessions:
                subdf = df[(df['task']==task) &
                           (df['condition']==condition) &
                           (df['session']==session) &
                           (df['patient_code']==patient_code)]
                counter[(patient_code,session)] = len(subdf)
        min_trials = np.min(list(counter.values()))
        if min_trials>=2:
            


    
