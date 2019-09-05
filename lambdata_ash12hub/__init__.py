"""
lambdata-ash12hub - A Collection of Data Science helper functions.
"""

import pandas as pd;
import numpy as np;
# from sklearn.model_selection import train_test_split;

def train_validation_test_split(x, y, train_size=0.8, val_size=0.1, test_size=0.1, random_state=None, shuffle=True):
    assert train_size + val_size + test_size == 1;

    x_train_val, x_test, y_train_val, y_test = train_test_split(x, y, test_size=test_size, random_state=random_state, shuffle=shuffle);

    x_train, x_val, y_train, y_val = train_test_split(x_train_val, y_train_val, test_size=val_size/(train_size+val_size), random_state=random_state, shuffle=shuffle);
    return x_train, x_val, x_test, y_train, y_val, y_test;

def split_date(df, date_column):
    df = df.copy();
    df[date_column] = pd.to_datetime(df[date_column], infer_datetime_format=True);

    df['date'] = df[date_column].dt.date;
    df['month'] = df[date_column].dt.month;
    df['year'] = df[date_column].dt.year;
    return df['date'], df['month'], df['year'];

def add_list_as_new_column(data_frame, new_list, new_list_name):
    data_frame[new_list_name] = new_list;
    return;