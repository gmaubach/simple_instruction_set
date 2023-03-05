#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
get_file

Load data from a text, csv or xls(x) file into a dataframe.

Author: Georg Maubach
Email: georg.maubach@la-ido.de
Version: 1.0.0
Date: 2023-03-05
"""
#--------1-------2---------3---------4---------5---------6---------7---------8

# Imports
import argparse
import pandas as pd
import openpyxl
from typing import Final

# Constants
MODULE_NAME: Final[str] = "get_file.py"

# Functions
def get_file(file_path, file_format=None, usecols=None, info=False):
    """Reads a data file into a pandas DataFrame.

    Args:
        file_path (str): The file path of the data file to be read.
        file_format (str, optional): The format of the data file. 
            If None, the format is inferred from the file extension.
        usecols (list, optional): A list of column names or column
            indices to be read. If None, all columns are read.
        info (bool, optional): If True, print variable names, head
            and tail of the dataframe.

    Returns:
        pandas.DataFrame: A pandas DataFrame containing the data
            from the input file.

    Examples:
        ```
        df = get_file('example.xlsx', print_vars=True)
        ```
                   
    Calling options:
        ```
        {options}     
        ```
    """
    # Infer the file format from the file extension if it is not specified
    if file_format is None:
        file_extension = file_path.split('.')[-1]
        if file_extension in ['txt', 'csv']:
            file_format = 'csv'
        elif file_extension in ['xls', 'xlsx']:
            file_format = 'xlsx'
        else:
            raise ValueError(
           'Invalid file format. Supported formats are .txt, .csv, .xls, .xlsx'
           )

    # Read the data file into a DataFrame
    if file_format in ['txt', 'csv']:
        df = pd.read_csv(file_path, usecols=usecols)
    elif file_format in ['xls', 'xlsx']:
        df = pd.read_excel(file_path, engine = 'openpyxl', usecols=usecols)

    # Print variable names if requested
    if info:
        print('Dataset Info:')
        print("Variable names:", ", ".join(df.columns.tolist()))
        print("First rows: \n", df.head())
        print("Last rows: \n", df.tail())

    return df

def main():
    parser = argparse.ArgumentParser(
        description='Reads a data file into a pandas DataFrame.'
        )
    parser.add_argument(
        '--file',
        dest='file_path',
        help='The file path of the data file to be read.'
        )
    parser.add_argument(
        '--format',
        dest='file_format',
        choices=['csv', 'txt', 'xlsx', 'xls'],
        default=None,
        help='The format of the data file. If not specified, the format is inferred from the file extension.')
    parser.add_argument(
        '--usecols',
        nargs='+',
        help='A list of column names or column indices to be read.'
    )
    parser.add_argument(
        '--info',
        dest='info',
        action='store_true',
        help='If set, print the variable names of the read dataset.'
    )
    parser.add_argument(
        '--debug',
        dest='debug',
        action='store_true',
        help='If set, debug routines are run.'
    )

    args = parser.parse_args()

    file_path = args.file_path
    file_format = args.file_format
    usecols = args.usecols
    info = args.info
    debug = args.debug

    if debug:
        print(f"Arguments given:")
        print(f"file_path: {file_path}")
        print(f"file_format: {file_format}")
        print(f"usecols: {usecols}")
        print(f"info: {info}")
        print(f"debug: {debug}\n")

    # Call the `get_file` function with the command-line arguments
    df = get_file(
        file_path,
        file_format=file_format,
        usecols=usecols,
        info=info)

    if debug:
        print("Dataset: \n", df)

    print(f"Execution complete: {MODULE_NAME}")

# Begin
if __name__ == '__main__':
    main()
# End .

# **./.**


