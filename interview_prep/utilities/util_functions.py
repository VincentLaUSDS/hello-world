"""Miscellaneous Utility Functions"""
import csv
import git
import logging
import tempfile

import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

LOGGER = logging.getLogger(__name__)


def get_git_root(path):
    """Return Top Level Git Repository directory given path"""
    git_repo = git.Repo(path, search_parent_directories=True)
    git_root = git_repo.git.rev_parse("--show-toplevel")
    return git_root


def custom_round(x, base=5):
    return base * round(x / base)


def check_missing_values(data):
    """Checks Missing Values By Column in Data"""
    df_count_missing = pd.DataFrame({
        'number_total_rows': data.shape[0],
        'number_missing_rows': data.isnull().sum(),
        'percentage': data.isnull().mean()})
    return df_count_missing


def one_hot_encoding(data, one_hot_column, drop_first=False, dummy_na=True, keep_original=True):
    """Returns Merged DataFrame with One Hot Encoded Column"""
    one_hot = pd.get_dummies(data[one_hot_column], prefix=one_hot_column, drop_first=drop_first, dummy_na=dummy_na)
    data = pd.concat([data, one_hot], axis=1)

    if keep_original:
        return data
    else:
        data.drop([one_hot_column], axis=1, inplace=True)
        return data


def compare_boolean_outcome_by_group(data, outcome, grouping):
    """
    Return an aggregate dataframe that compares mean, sum, and count of boolean outcome by group

    Keyword Args:
      data: DataFrame to group by
      outcome: The Outcome Column
      grouping: The Grouping Column
    """
    grouped = data[[outcome, grouping]].groupby(grouping).agg({outcome: ['mean', 'sum', 'count']})
    grouped.columns = grouped.columns.swaplevel().map('_'.join)
    return grouped


def create_corr_heatmap(data):
    """
    Create the correlation heatmap of a dataframe

    Taken from: https://seaborn.pydata.org/examples/many_pairwise_correlations.html
    Keyword Args:
      data: DataFrame with data
    """
    corr = data.corr()
    sns.set(style="white")

    # Generate a mask for the upper triangle
    mask = np.zeros_like(corr, dtype=np.bool)
    mask[np.triu_indices_from(mask)] = True

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Generate a custom diverging colormap
    cmap = sns.diverging_palette(220, 10, as_cmap=True)

    # Draw the heatmap with the mask and correct aspect ratio
    heatmap = sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
        square=True, linewidths=.5, cbar_kws={"shrink": .5})
    return heatmap


def split_dataset(dataset, train_percentage, feature_headers, target_header):
    """
    Split the dataset with train_percentage
    
    Keyword Args:
    dataset: The Actual Dataset
    train_percentage: Percentage of Dataset to split into Training
    feature_headers: columns that are features to include
    target_header: column that is the outcome variable of interest
    :return: train_x, test_x, train_y, test_y
    """

    # Split dataset into train and test dataset
    train_x, test_x, train_y, test_y = train_test_split(dataset[feature_headers], dataset[target_header],
                                                        train_size=train_percentage)
    return train_x, test_x, train_y, test_y


def df_to_sql(db_conn, df, table_name, schema, required_type_map=None,
              use_index=False,
              sep='|',
              encoding='utf8',
              temp_file_func=tempfile.SpooledTemporaryFile,
              if_exists='replace',
              chunksize=None):
    """Helper for writing a pandas.Dataframe to SQL
    Args:
        db_conn (sqlalchemy.engine.Connection):
        df (pandas.DataFrame): the dataframe to write to sql
        table_name (str): the output table name
        schema (str): the output schema name
        required_type_map (dict): optional mapping of column names to sqlalchemy types
        use_index (boolean):
        sep (str): separator for temp file
        encoding (str): encoding for temp file
        temp_file_func (tempfile.TemporaryFile): function to call for building
            temp file. Passed as default arg so this works in tests when mocking
            out the filesystem
        if_exists (str): what to do if table exists. 'append' and 'replace' are supported
    Has been benchmarked to be faster than pd.to_sql, odo, and other pandas hacks
    """
    assert if_exists in ['append', 'replace']
    if required_type_map and \
            any(col not in df.columns for col in required_type_map.keys()):  # pragma: no cover
        raise TypeError('required_type_map contains invalid columns.')

    # Use DF to create empty table
    LOGGER.info('Replacing %s', table_name)
    df[:0].to_sql(table_name, db_conn,
                  if_exists=if_exists,
                  index=use_index,
                  schema=schema,
                  dtype=required_type_map or {})

    with temp_file_func(mode='w+', suffix='.csv') as tmp_file:
        df.to_csv(tmp_file, sep=sep, header=False, quoting=csv.QUOTE_NONE, quotechar='',
                  escapechar='\\', encoding=encoding, index=use_index)
        tmp_file.seek(0)

        with db_conn.connection.cursor() as cursor:
            cursor.copy_from(tmp_file, '.'.join([schema, table_name]), sep=sep, null='')
            LOGGER.info('Completed copy from for %s', table_name)
