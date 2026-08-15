import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import glob,os,sys,shutil
import re

def get_date_time(filename):
    date_regex = r'\d{4}-\d{2}-\d{2}'
    time_regex = r'[-_]\d{2}-\d{2}-\d{2}'
    try:
        date_match = re.search(date_regex,filename)
        date = date_match.group()
        time_match = re.search(time_regex,filename)
        time = time_match.group()[1:]
    except AttributeError as ae:
        sys.exit('%s failed to contain a date of the form YYYY-MM-DD or time of the form _HH-mm-SS'%filename)
    return (date,time)

def get_all_date_times(folder):
    out = []
    for f in glob.glob(os.path.join(folder,'*.csv')):
        out.append(get_date_time(f))
    return list(set(out))


def organize_by_protocol(folder,delete_old=False):
    # search through all the 'measurement_inform' files in a folder, and
    # use them to create protocol subfolders and copy the csv files into those
    mi_files = glob.glob(os.path.join(folder,'*measurement_inform*.csv'))
    for mi_file in mi_files:
        mi_df = pd.read_csv(mi_file)
        protocol = mi_df['protocol_name'].iloc[0]
        date_time_stamp = get_date_time(mi_file)
        protocol_subfolder = os.path.join(folder,protocol.replace(' ','_'))
        os.makedirs(protocol_subfolder,exist_ok=True)
        
        # fragile: are there other files that might match this filter?
        filt = date_time_stamp[0]+'*'+date_time_stamp[1]+'*'
        filt = os.path.join(folder,filt)
        matching_files = glob.glob(filt)
        for mf in matching_files:
            out_filename = os.path.join(protocol_subfolder,os.path.split(mf)[1])
            if delete_old:
                shutil.move(mf,out_filename)
                print('moving %s -> %s'%(mf,out_filename))
            else:
                shutil.copy(mf,out_filename)
                print('copying %s -> %s'%(mf,out_filename))


def folder_report(folder):
    report = '%s\n'%folder
    
    # use files whose names contain "measurement_inform" to determine
    # the number of complete datasets there are
    mi_files = sorted(glob.glob(os.path.join(folder,'*measurement_inform*.csv')))
    for mi_file in mi_files:
        date,time = get_date_time(mi_file)
        mi_df = pd.read_csv(mi_file)
        
        patient_code = mi_df['patient_code'].iloc[0]
        protocol_name = mi_df['protocol_name'].iloc[0]

        # concatenate the date and time to search for every file containing each combination
        date_time = '%s_%s'%(date,time)
        file_subset = sorted(glob.glob(os.path.join(folder,'*%s*.csv'%date_time)))
        
        report = report + '\t%s\t%s\t%s\t%s\n'%(patient_code,date,time,protocol_name)
        
        for subset_filename in file_subset:
            report = report + '\t\t%s\n'%subset_filename

    return report

def get_files_for_protocol(folder,protocol):
    date_times = get_all_date_times(folder)
    out = []
    for date_time in date_times:
        filt = date_time[0]+'*'+date_time[1]
        mi_filenames = glob.glob(os.path.join(folder,'*%s*_measurement_inform*.csv'%filt))
        if len(mi_filenames)==0:
            continue
        mi_filename = mi_filenames[0]
        mi_df = pd.read_csv(mi_filename)
        protocol_name = mi_df['protocol_name'].iloc[0]
        if protocol_name.find(protocol)==-1:
            continue
        out = out + glob.glob(os.path.join(folder,'*%s*.csv'%filt))
    return out



class Dataset:

    def __init__(self,filename,skiprows=4,delimiter='_'):
        self.filename = filename
        self.skiprows = skiprows
        self.delimiter = delimiter

    def get_df(self):
        header = self.digest_header()
        df = pd.read_csv(self.filename,skiprows=self.skiprows,header=None,names=header)
        return df
    
        
    def digest_header(self):
        header_df = pd.read_csv(self.filename,nrows=self.skiprows,header=None)
        header_data = []
        row_lengths = []
        for idx,row in header_df.iterrows():
            row_list = list(row)
            row_lengths.append(len(row_list))
            header_data.append(row_list)

        assert all(np.array(row_lengths)==np.max(row_lengths))
        ncols = row_lengths[0]
        
        columns = []

        for row in header_data:
            last = ''
            for idx in range(len(row)):
                item = row[idx]
                if type(item)==float:
                    if np.isnan(item):
                        row[idx] = last
                        continue
                last = item

        for col in range(ncols):
            columns.append(self.delimiter.join([r[col] for r in header_data if len(r[col])]))

        return columns

