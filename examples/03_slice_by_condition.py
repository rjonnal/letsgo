import letsgo as lg
import config as cfg

"""This script illustrates how to divide the datasets by task,
condition, patient_code, etc., in order to implement reliability
calculations or hypothesis testing. Note that this labeling
is now built into letsgo.get_all_datasets, via the function
letsgo.label_datasets_with_condition_and_session."""

datasets = lg.get_all_datasets(cfg.data_root)

WR_datasets = [ds for ds in datasets if ds.condition=='WR']
SD_datasets = [ds for ds in datasets if ds.condition=='SD']

print(WR_datasets)
print(SD_datasets)
