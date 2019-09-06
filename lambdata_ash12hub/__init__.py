"""
lambdata-ash12hub - A Collection of Data Science helper functions.
"""

import pandas as pd
import numpy as np


def train_validation_test_split(
        x, y, train_size=0.8, val_size=0.1, test_size=0.1,
        random_state=None, shuffle=True):
    assert train_size + val_size + test_size == 1

    x_train_val, x_test, y_train_val, y_test = train_test_split(
        x, y, test_size=test_size, random_state=random_state, shuffle=shuffle)

    x_train, x_val, y_train, y_val = train_test_split(
        x_train_val, y_train_val, test_size=val_size/(train_size+val_size),
        random_state=random_state, shuffle=shuffle)

    return x_train, x_val, x_test, y_train, y_val, y_test


def split_date_list(date_list):
    date_list = pd.to_datetime(date_list, infer_datetime_format=True)
    day = date_list.dt.day
    month = date_list.dt.month
    year = date_list.dt.year
    return day, month, year


def add_new_column(new_list):
    new_column = pd.Series(new_list)
    return new_column
