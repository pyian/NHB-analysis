
# coding: utf-8

# Import tdms to Python
# ============
# 2017-07-22 23:00
#
# 1. Get tdms file
# 2. Cleaning
# 3. Convert to pandas df
# 4. Save df as pickle

import pandas as pd
import re
from nptdms import TdmsFile
from datetime import datetime, timedelta


if __name__ == '__main__':
    print('hi')


def to_pd(path):

    def get_tdms_file(path):
        # file_name = 'UNH-01_R131_07_05_2017_03_01_40_Decimate_All'
        # extension = '.tdms'
        tdms_file = TdmsFile(path)
        return tdms_file

    def get_file_name(path):
        regex = '(UNH-.+).tdms'
        matches = re.findall(regex, path)
        return matches[0]

    def extract_start_time(file_name):
        regex = "_(\d\d_\d\d_\d{4}_\d\d_\d\d_\d\d)"
        matches = re.findall(regex, file_name)

        values = matches[0].split('_')

        time_list = []

        time_list.append(values[2])

        for i in range(len(values)):
            if i != 2:
                time_list.append(values[i])

        start_time = datetime(*map(int, time_list))
        # print('Start time: ', start_time)
        return start_time

    def to_df(tdms_file, start_time):

        temp = []

        for key, value in tdms_file.objects.items():
            try:
                if 'All' in key:
                    if 'Time' in key:  # convert and add start time for 'Time'
                        time_stamp = []
                        for i in value.data:
                            time_stamp.append(
                                start_time + timedelta(seconds=i))
                        temp.append((key, pd.Series(data=time_stamp)))
                    elif value.has_data:
                        temp.append((key, pd.Series(data=value.data)))
            except:
                df = pd.DataFrame.from_items(temp)
                break

        df = pd.DataFrame.from_items(temp)

        return df

    def clean_df(df):

        def clean_col_names(df):
            regex = "([A-z-0-9]+)\'$"

            col_name = []
            for col in df.columns:
                col_name.append(re.findall(regex, col)[0])

            df.columns = col_name

            return df

        def time_as_index(df):
            df['Time'] = pd.to_datetime(df['Time'])
            df = df.set_index('Time')

            return df

        def drop_null(df):
            null_cols = df.columns[df.isnull().any()].tolist()
            df = df.drop(null_cols, axis=1)

            return df

        df = clean_col_names(df)
        df = time_as_index(df)
        df = drop_null(df)

        return df

    file_name = get_file_name(path)
    tdms_file = get_tdms_file(path)
    start_time = extract_start_time(file_name)
    df = to_df(tdms_file, start_time)
    df = clean_df(df)

    # Save df as pickle
    pd.to_pickle(df, file_name + '.p')

    # print(df.head())

    # print('Import {} sucessfully'.format(file_name))
    print('{} saved'.format(file_name + '.p'))
    return file_name + '.p'
