import letsgo as lg

"""This script illustrates how to create a single Dataset
object by passing its constructor a XXX_measurement_inform.csv
file."""

mi_filename = '/home/rjonnal/Dropbox/Data/eye_tracking/NeuroSleep_011/NeuroSleep_011_SD_01/2026-06-17_12-59-44_measurement_inform.csv'

dataset = lg.Dataset(mi_filename)

