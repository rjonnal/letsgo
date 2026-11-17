import letsgo as lg
import config as cfg
import pandas as pd

"""This script illustrates how to create a simple report from a
list of datasets."""

datasets = lg.get_all_datasets(cfg.data_root)

# The report will be a CSV file with the following columns:
# task, condition, patient_code, session, number of trials.

trial_counts = {}

for ds in datasets:
    trial_counter_key = (ds.task,ds.condition,ds.patient_code,ds.session)
    if not trial_counter_key in trial_counts.keys():
        trial_counts[trial_counter_key] = 1
    else:
        trial_counts[trial_counter_key] += 1

rows = []

for k in trial_counts.keys():
    row = [k[0],k[1],k[2],k[3],trial_counts[k]]
    rows.append(row)

columns = ['task','condition','patient_code','session','n_trials']
    
df = pd.DataFrame(rows,columns=columns)
df.to_csv('report.csv',index=False)
    
