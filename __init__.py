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

    # find all *measurement_inform.csv files below this point in
    # the file system
    mi_files = path.rglob('*measurement_inform.csv')

    mi_files = [str(mi_file) for mi_file in mi_files]

    # output data structure
    all_datasets = []

    for mi_file in mi_files:
        all_datasets.append(Dataset(mi_file))

    label_datasets_with_condition_and_session(all_datasets)

    all_datasets.sort()
    
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


def label_datasets_with_condition_and_session(dataset_list):
    # a regex pattern that returns 5 groups of characters:
    # 1) the head of the location (everything before the session folder), any string (.*)
    # 2) the digits of the patient ID (not used, but could be used for integrity-check) (\d+)
    # 3) the condition--any string (.*)
    # 4) the digits of the session (\d+)
    # 5) the tail of the location (everthing after the session number) (.*)
    pattern = re.compile(r"(.*)NeuroSleep_(\d+)_(.*)_(\d+)(.*)")

    # Now iterate through and label the datasets by condition, and add
    # the condition as a property. We also add the session number. Both
    # use regex matching on the filename.
    for ds in dataset_list:
        loc = ds.dataset_location
        match = None
        for tok in path_parts(loc):
            match = pattern.match(loc)
            if match:
                break
        h,patient_id_number,condition,session,t = match.groups()
        ds.condition = condition
        ds.session = int(session)


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


def path_parts(s):
    p = pathlib.Path(s)
    return list(p.parts)

# each csv file type has a different number of header rows
# we need to know how many there are for each type in order
# to convert to pandas DataFrame
n_header_rows = {'distributional_aggregated':3,'drift_non_aggregated':4,'measurement_inform':1,'non_distributional_parameters':3,'pso_non_aggregated':4,'saccade_non_aggregated':4,'saccade_with_pso_non_aggregated':4,'trajectories':2,'trial_non_aggregated':4}

class Dataset:

    def __init__(self,mi_file,header_delimiter='_',load_trajectories=False):
        self.dataframe_dictionary = {}
        self.filename_dictionary = {}
        self.header_delimiter = header_delimiter
        self.timestamp = get_timestamp(mi_file)
        self.dataset_location = os.path.split(mi_file)[0]

        csv_filter = os.path.join(self.dataset_location,self.timestamp)+'*.csv'
        csv_file_list = glob.glob(csv_filter)
        
        for csv_file in csv_file_list:
            csv_file = str(csv_file)
            for k in n_header_rows.keys():
                if csv_file.find(k)>-1:
                    self.filename_dictionary[k] = csv_file
                    
        midf = self.get_dataframe('measurement_inform')
        self.patient_code = midf['patient_code'].iloc[0]
        self.eye = midf['which_eye'].iloc[0]
        self.task = midf['protocol_name'].iloc[0]
        self.condition = None
        self.session = -1

    def list_dataframes(self):
        for k in n_header_rows.keys():
            print('%s: '%k,end='')
            try:
                csv_filename = self.filename_dictionary[k]
            except KeyError as ke:
                csv_filename = 'not found'
            print(csv_filename)

    def get_dataframe(self,dataframe_key):
        skiprows = n_header_rows[dataframe_key]
        filename = self.filename_dictionary[dataframe_key]
        header = self.digest_header(filename,skiprows)
        df = pd.read_csv(filename,skiprows=skiprows,names=header)
        return df

    def __str__(self):
        out = ''
        out = out + 'location: %s\n'%self.dataset_location
        out = out + 'timestamp: %s\n'%self.timestamp
        out = out + 'subject: %s\n'%self.patient_code
        out = out + 'task: %s\n'%self.task
        out = out + 'condition: %s\n'%self.condition
        out = out + 'session: %d\n'%self.session
        return out

    def __gt__(self,other):
        return self.__str__().__gt__(other.__str__())

    def __repr__(self):
        return self.__str__().replace('\n',' / ')
                    
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

    def get_aggregated_params(self):
        # return a dictionary containing name-value pairs
        # each name is a tuple (A,B), where
        # A is the name of a column in distributional_aggregated
        # and B is the aggregation method (MEAN, STD, etc.)
        # or (A,None), where A is the name of a column in
        # non_distributional_parameters
        # each value is the corresponding value
        out = {}
        out['patient_code'] = self.patient_code
        out['task'] = self.task
        out['session'] = self.session
        out['timestamp'] = self.timestamp
        out['condition'] = self.condition
        out['eye'] = self.eye
        out['dataset_location'] = self.dataset_location
        
        df = self.get_dataframe('distributional_aggregated')
        columns = [str(item) for item in df.columns]
        rows = list(df['parameter_axis_unit'])
        for c in columns:
            if c=='parameter_axis_unit':
                continue
            for r in rows:
                key = (c,r)
                value = df[df['parameter_axis_unit']==r][c].iloc[0]
                if type(value)==np.float64:
                    value=float(value)
                out[key] = value

        df = self.get_dataframe('non_distributional_parameters')
        columns = [str(item) for item in df.columns]
        for c in columns:
            if c=='parameter_axis_unit':
                continue
            key = (c,None)
            value = df[c].iloc[0]
            out[key] = value

        
        return out
