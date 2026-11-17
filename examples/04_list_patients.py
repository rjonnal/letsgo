import letsgo as lg
import config as cfg

"""This script illustrates how to identify all of the patient_codes
in a list of datasets and print them out."""

datasets = lg.get_all_datasets(cfg.data_root)

# first make a list of all patient codes, with repeats
patient_codes = [ds.patient_code for ds in datasets]

print(patient_codes)

# Notice that there are inconsistencies in patient codes:
# NeuroSleep013 is the same patient as NeuroSleep_013, but
# they're programatically different, so we generate unique
# patient_codes and list them.

unique_patient_codes = list(set(patient_codes))

print(unique_patient_codes)
