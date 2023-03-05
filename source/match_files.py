#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
match_files

Matches two pandas DataFrames based on common columns.

Author: Georg Maubach
Email: georg.maubach@la-ido.de
Version: 1.0.0
Date: 2023-03-05

Example:
    ```
    match_files(left_df, right_df, on='variable_name', how='outer')
    ```

Calling:
    ```
    match_files.py --left_df test_existing_data.csv --right_df test_new_data.csv --on id --how full --debug
    ```

See Also:
    * `related documentation <https://example.com>`_
"""
#--------1-------2---------3---------4---------5---------6---------7---------8

# Imports
import argparse
import pandas as pd
from typing import Final

# Constants
MODULE_NAME: Final[str] = "match_files.py"

# Functions
def match_files(left_df, right_df, on=None, how='inner'):
    """Matches two pandas DataFrames based on common columns.

    Args:
        left_df (pandas.DataFrame): The left dataframe to be matched.
        right_df (pandas.DataFrame): The right dataFrame to be matched.
        on (str or list of str, optional): The column name or names to join on.
            If None, the function will try to infer the common columns
            to join on.
        how (str, optional): The type of join to perform. 
            Must be one of 'inner', 'left', 'right', or 'outer'.
            'full' and 'full outer' are used as synonyms for 'outer'.
            Default is 'inner'.

    Returns:
        pandas.DataFrame: A merged DataFrame containing the matching rows
             from both DataFrames.

    Raises:
        ValueError: If no common columns to join on or
            multiple common columns to join on.

    Notes:
        - The `left_df` DataFrame is used as the left dataframe
              in the join operation that is used as the base dataframe
              the right data is matched to.
        - The `right_df` DataFrame is used as the right dataFrame
              in the join operation that is used as the secondary dataframe
              to match to the base dataframe.
    
    Example:
        ```
        match_files(left_df, right_df, on='variable_name', how='inner')
        ```
    """
    
    # Infer common columns to join on if not specified
    if on is None:
        common_columns = list(set(left_df.columns) & set(right_df.columns))
        if len(common_columns) == 0:
            raise ValueError('No common columns to join on.')
        elif len(common_columns) > 1:
            raise ValueError(
                'Multiple common columns to join on. Please specify the join column(s) explicitly.'
                )
        else:
            on = common_columns[0]

    # Perform the join based on the specified type
    if how == 'inner':
        merged_df = pd.merge(
            left_df,
            right_df,
            on=on,
            how=how,
            suffixes=('_left', '_right')
            )
    elif how == 'left':
        merged_df = pd.merge(
            left_df,
            right_df,
            on=on,
            how=how,
            suffixes=('_left', '_right')
            )
    elif how == 'right':
        merged_df = pd.merge(
            left_df,
            right_df,
            on=on,
            how=how,
            suffixes=('_left', '_right')
            )
    elif how in ('outer', 'full', 'full outer'):
        merged_df = pd.merge(
            left_df,
            right_df,
            on=on,
            how='outer',
            suffixes=('_left', '_right'))
    else:
        raise ValueError(
            'Argument "on" not in (left, right, inner, outer, full, full outer).'
        )

    return merged_df
    
def main():
    parser = argparse.ArgumentParser(
        description='Match two pandas dataframes based on common columns.'
        )
    parser.add_argument(
        '--left_df',
        dest='left_df',
        default='../data/test_existing_data.csv',
        help='The path to the left dataframe to be matched.'
        )
    parser.add_argument(
        '--right_df',
        dest='right_df',
        default='../data/test_new_data.csv',
        help='The path to the right dataframe to be matched.'
        )
    parser.add_argument(
        '-o', '--on',
        dest='on',
        nargs='+',
        help='The column name or names to join on.'
        )
    parser.add_argument(
        '-t', '--how',
        dest='how',
        choices=['inner', 'left', 'right', 'outer', 'full', 'full outer'],
        default='inner',
        help='The type of join to perform.')

    parser.add_argument(
        '--debug',
        dest='debug',
        action='store_true',
        default='False',
        help='If set, debug routines are run.'
    )

    args = parser.parse_args()

    left_df = args.left_df
    right_df = args.right_df
    on = args.on
    how = args.how
    debug = args.debug

    if debug:
        print(f"Arguments given:")
        print(f"left_df: {left_df}")
        print(f"right_df: {right_df}")
        print(f"on: {on}")
        print(f"how: {how}")
        print(f"debug: {debug}\n")

    left_df = pd.read_csv(left_df)
    right_df = pd.read_csv(right_df)
    merged_df = match_files(
        left_df = left_df,
        right_df = right_df,
        on = on,
        how = how)
        
    if debug:
        print(merged_df)
    
    print(f"Execution complete: {MODULE_NAME}")

# Begin
if __name__ == "__main__":
    main()
# End .

# **./.**


