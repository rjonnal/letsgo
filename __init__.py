import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

class Dataset:

    def __init__(self,excel_filename):

        self.filename = excel_filename
        self.data_dict = pd.read_excel(excel_filename,sheet_name=None)
        self.sheet_names = list(self.data_dict.keys())


    def digest_header(self,sheet_name,skiprows=4):
        header_df = pd.read_excel(self.filename,sheet_name=sheet_name,nrows=skiprows,header=None)
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
            columns.append(';'.join([r[col] for r in header_data]))

        return columns

    def get_df(self,sheet_name,skiprows=4):
        cols = self.digest_header(sheet_name,skiprows)
        df = pd.read_excel(self.filename,sheet_name=sheet_name,skiprows=skiprows,header=None,names=cols)
        return df
        
    def get_split_dfs(self,sheet_name,skiprows=4,col_to_split='parameter;axis;unit;'):
        df = self.get_df(sheet_name,skiprows)
        params = set(list(df[col_to_split]))
        out = {}
        for param in params:
            out[param] = df[df[col_to_split]==param]
        return out
    
        
    def list_sheets(self):
        print('Sheets in %s:'%self.filename)
        for idx,k in enumerate(sorted(self.data_dict.keys())):
            v = self.data_dict[k]
            print('%03d (%s): dataframe with %04d rows and columns %s'%(idx,k,len(v),v.columns))

        
