import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

class Dataset:

    def __init__(self,excel_filename,delimiter='|'):

        self.filename = excel_filename
        self.data_dict = pd.read_excel(excel_filename,sheet_name=None)
        self.sheet_names = list(self.data_dict.keys())
        self.delimiter = delimiter
        self.col_to_split = delimiter.join(['parameter','axis','unit'])
        
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
            columns.append(self.delimiter.join([r[col] for r in header_data if len(r[col])]))

        return columns

    def get_df(self,sheet_name,skiprows=4):
        cols = self.digest_header(sheet_name,skiprows)
        df = pd.read_excel(self.filename,sheet_name=sheet_name,skiprows=skiprows,header=None,names=cols)
        return df
        
    def get_split_dfs(self,sheet_name,skiprows=4):
        df = self.get_df(sheet_name,skiprows)
        params = set(list(df[self.col_to_split]))
        out = {}
        for param in params:
            out[param] = df[df[self.col_to_split]==param]
        return out
    
        
    def list_sheets(self):
        print('Sheets in %s:'%self.filename)
        for idx,k in enumerate(sorted(self.data_dict.keys())):
            v = self.data_dict[k]
            print('%03d (%s): dataframe with %04d rows and columns %s'%(idx,k,len(v),v.columns))

        
    def column_name_to_text(self,col_name,break_line=False):
        """Assume that the column name consists of three strings joined by the
        delimiter. We want to split the string into three, then delimit the first
        two with a comma and put parens around the third (unit). Replace underscores
        with spaces as well."""
        toks = col_name.split(self.delimiter)
        toks = [tok.replace('_',' ') for tok in toks]
        if not break_line:
            return '%s, %s (%s)'%tuple(toks)
        else:
            return '%s\n%s (%s)'%tuple(toks)
