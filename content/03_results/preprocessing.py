'''
Module containing data preprocessing code.

This was created to remove the amount of code included in each jupyter notebook.
For an overview and explanation of the code please see 01_preprocessing.ipynb

'''

import pandas as pd
import numpy as np

# Constants

FILE_NAME = 'https://raw.githubusercontent.com/TomMonks/' \
    + 'des_sharing_lit_review/main/data/share_sim_data_extract.csv'

# used to drop redudant manuscript fields outputted by zotero 
# e.g. keywords and abstracts.
COLS_TO_KEEP = [2, 3, 4, 5, 6, 7, 10, 11, 44, 45, 46, 47, 
                48, 49, 50, 51, 52, 52, 53, 54, 55]

def trim_columns(df):
    '''
    Remove fields that are not needed for the clean
    analysis dataset.
    
    Uses the COLS_TO_KEEP constant list.
    
    Params:
    -------
    df - pd.DataFrame
        The raw data
    
    Returns:
    --------
    pd.DataFrame
    
    '''
    return df[df.columns[COLS_TO_KEEP]]

def cols_to_lower(df):
    '''
    Convert all column names in a dataframe to lower case
    
    Params:
    ------
    df - pandas.DataFrame
    
    Returns:
    -------
    pandas.DataFrame
    '''
    new_cols = [c.lower() for c in df.columns]
    df.columns = new_cols
    return df

def load_clean_dataset(file_name):
    '''
    Loads a cleaned verion of the dataset
    
    1.  Trims the columns to only those relevant to the analysis
    2.  Replaces space in the column names with "_"
    3.  Converts all column names to lower case
    4.  Convert relevant cols to Categorical data type
    5.  Performs remaining type conversions.
    '''
    labels = {'Item Type': 'item_type',
               'Publication Year': 'pub_yr',
               'Publication Title': 'pub_title'}

    type_conversions = {'pub_yr': 'int'}
    
    recoded_types = {'item_type': {'bookSection':'book'},
                     'reporting_guidelines_mention': {'ISPOR-SMDM': 'ISPOR',
                                                      '0': 'None'}}

    clean = (pd.read_csv(file_name)
             .pipe(trim_columns)
             .rename(columns=labels) 
             .pipe(cols_to_lower)
             .replace(recoded_types)
             .assign(study_included=lambda x: 
                         pd.Categorical(x['study_included']),
                     model_code_available=lambda x: 
                         pd.Categorical(x['model_code_available']),
                     reporting_guidelines_mention=lambda x: 
                         pd.Categorical(x['reporting_guidelines_mention']),
                     covid=lambda x: pd.Categorical(x['covid']),
                     foss_sim=lambda x: pd.Categorical(x['foss_sim']),
                     item_type=lambda x: pd.Categorical(x['item_type']))
            .astype(type_conversions)
            
    )

    return clean
