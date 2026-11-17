import letsgo as lg
import config as cfg

"""This script illustrates how to divide the datasets by task,
condition, patient_code, etc., in order to implement reliability
calculations or hypothesis testing."""

datasets = lg.get_all_datasets(cfg.data_root)

# now iterate through and label the datasets by condition
for ds in datasets:
    loc = ds.dataset_location
    for condition in ['WR','SD']:
        if loc.find(condition)>-1:
            ds.condition = condition

WR_datasets = [ds for ds in datasets if ds.condition=='WR']
SD_datasets = [ds for ds in datasets if ds.condition=='SD']



print(WR_datasets)
print(SD_datasets)
