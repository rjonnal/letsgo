import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import glob,os,sys,shutil
import re
import pathlib

def get_all_datasets(data_root):
    # create a path object that represents
    # the data_root point in the file system
    path = pathlib.Path(data_root)

    # find all .csv files below this point in
    # the file system
    csv_files = path.rglob('*.csv')

    # use get_timestamp to get all timestamps from the
    # file list
    all_timestamps = []
    for csv_file in csv_files:
        timestamp = get_timestamp(csv_file)
        if timestamp is None:
            continue
        all_timestamps.append(timestamp)

    # use set to extract unique matches
    unique_timestamps = set(all_timestamps)

    # output data structure
    all_datasets = []

    # instantiate a Dataset object using the list
    # of csv files corresponding to a single recording:
    for timestamp in unique_timestamps:
        dataset_files = list(path.rglob('*%s*.csv'%timestamp))
        n_files = len(dataset_files)
        if n_files!=9:
            print('Warning: %d files found with timestamp %s.'%(n_files,timestamp))
        all_datasets.append(Dataset(dataset_files,timestamp))

    return all_datasets

def get_timestamp(filename):
    filename = str(filename)
    date_regex = r'\d{4}-\d{2}-\d{2}'
    time_regex = r'[_]\d{2}-\d{2}-\d{2}'
    try:
        date_match = re.search(date_regex,filename)
        date = date_match.group()
        time_match = re.search(time_regex,filename)
        time = time_match.group()[1:]
    except AttributeError as ae:
        print('%s does not contain a timestamp; skipping.'%filename)
        return None
    return date+'_'+time

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


def organize_by_task(folder,delete_old=False):
    # search through all the 'measurement_inform' files in a folder, and
    # use them to create task subfolders and copy the csv files into those
    mi_files = glob.glob(os.path.join(folder,'*measurement_inform*.csv'))
    for mi_file in mi_files:
        mi_df = pd.read_csv(mi_file)
        task = mi_df['task_name'].iloc[0]
        date_time_stamp = get_date_time(mi_file)
        task_subfolder = os.path.join(folder,task.replace(' ','_'))
        os.makedirs(task_subfolder,exist_ok=True)
        
        # fragile: are there other files that might match this filter?
        filt = date_time_stamp[0]+'*'+date_time_stamp[1]+'*'
        filt = os.path.join(folder,filt)
        matching_files = glob.glob(filt)
        for mf in matching_files:
            out_filename = os.path.join(task_subfolder,os.path.split(mf)[1])
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
        task_name = mi_df['task_name'].iloc[0]

        # concatenate the date and time to search for every file containing each combination
        date_time = '%s_%s'%(date,time)
        file_subset = sorted(glob.glob(os.path.join(folder,'*%s*.csv'%date_time)))
        
        report = report + '\t%s\t%s\t%s\t%s\n'%(patient_code,date,time,task_name)
        
        for subset_filename in file_subset:
            report = report + '\t\t%s\n'%subset_filename

    return report

def get_files_for_task(folder,task):
    date_times = get_all_date_times(folder)
    out = []
    for date_time in date_times:
        filt = date_time[0]+'*'+date_time[1]
        mi_filenames = glob.glob(os.path.join(folder,'*%s*_measurement_inform*.csv'%filt))
        if len(mi_filenames)==0:
            continue
        mi_filename = mi_filenames[0]
        mi_df = pd.read_csv(mi_filename)
        task_name = mi_df['task_name'].iloc[0]
        if task_name.find(task)==-1:
            continue
        out = out + glob.glob(os.path.join(folder,'*%s*.csv'%filt))
    return out

# each csv file type has a different number of header rows
# we need to know how many there are for each type in order
# to convert to pandas DataFrame
n_header_rows = {'distributional_aggregated':3,'drift_non_aggregated':4,'measurement_inform':1,'non_distributional_parameters':3,'pso_non_aggregated':4,'saccade_non_aggregated':4,'saccade_with_pso_non_aggregated':4,'trajectories':2,'trial_non_aggregated':4}

class Dataset:

    def __init__(self,csv_file_list,timestamp,header_delimiter='_'):
        self.dataframe_dictionary = {}
        self.filename_dictionary = {}
        self.header_delimiter = header_delimiter
        self.timestamp = timestamp
        for csv_file in csv_file_list:
            csv_file = str(csv_file)
            for k in n_header_rows.keys():
                if csv_file.find(k)>-1:
                    skiprows = n_header_rows[k]
                    header = self.digest_header(csv_file,skiprows)
                    self.filename_dictionary[k] = csv_file
                    self.dataframe_dictionary[k] = pd.read_csv(csv_file,skiprows=skiprows,names=header)
        midf = self.dataframe_dictionary['measurement_inform']
        self.patient_code = midf['patient_code'].iloc[0]
        self.eye = midf['which_eye'].iloc[0]
        self.task = midf['protocol_name'].iloc[0]

    def __str__(self):
        return '%s / %s / %s / %s'%(self.timestamp,
                                    self.patient_code,
                                    self.eye,
                                    self.task)
                    
    def digest_header(self,csv_file,skiprows):
        header_df = pd.read_csv(csv_file,nrows=skiprows,header=None)
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

        for col_idx in range(ncols):
            columns.append(self.header_delimiter.join([r[col_idx] for r in header_data if len(r[col_idx])]))

        for idx,col in enumerate(columns):
            if idx==0:
                continue
            while col in columns[:idx]:
                col = col+'_'
            columns[idx] = col

        return columns

