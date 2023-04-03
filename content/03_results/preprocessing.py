'''
Module containing data preprocessing code.

This was created to remove the amount of code included in each jupyter notebook.

For an overview and explanation of the code for the full dataset 
please see 01_preprocessing.ipynb

For an overview and explanation of the code the best practice audit please see
04_bpa_preprocessing.ipynb

'''

import pandas as pd
import numpy as np

# Constants

FILE_NAME = 'https://raw.githubusercontent.com/TomMonks/' \
    + 'des_sharing_lit_review/main/data/share_sim_data_extract.csv'

# used to drop redudant manuscript fields outputted by zotero 
# e.g. keywords and abstracts.
COLS_TO_KEEP = [2, 3, 4, 5, 6, 7, 10, 11, 44, 45, 46, 47, 
                48, 49, 50, 51, 52, 52, 53, 54, 55, 57]

# used to drop redudant fields not needed in BEST PRACTICE analysis.
COLS_TO_DROP = [5, 6, 8, 18, 24, 29, 33]

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

def drop_columns(df, to_drop):
    '''
    Remove fields that are not needed for the clean
    analysis best practice dataset.
    
    Uses the COLS_TO_DROP constant list.
    
    Params:
    -------
    df - pd.DataFrame
        The raw data
    
    Returns:
    --------
    pd.DataFrame
    
    '''
    return df.drop(df.columns[to_drop], axis=1)

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

def load_clean_bpa(file_name):
    '''
    Loads a cleaned verion of the BEST PRACTICE AUDIT dataset
    
    1.  Replaces space in the column names with "_" and renameds model doi col.
    2.  Converts all column names to lower case
    3.  Drop columns not needed for analysis
    4.  Recode values in Janssen method columns
    5.  Convert relevant cols to Categorical data type
    6.  Performs remaining type conversions.
    '''
    
    labels = {'DOI.1': 'model_has_doi',
              'Item Type': 'item_type',
              'Publication Year': 'pub_yr',
              'Publication Title': 'pub_title'}
    
    recoded = {'model_repo': {'Github':'GitHub'},
               'model_journal_supp': {'R model in word file':'Word doc'},
               'model_personal_org': {'personex': 'Organisational website',
                                      'Personex': 'Organisational website',
                'https://resp.core.ubc.ca/research/Specific_Projects/EPIC':
                 'Organisational website'}}
    
    clean = (pd.read_csv(file_name)
               .rename(columns=labels)
               .pipe(cols_to_lower)
               .pipe(drop_columns, COLS_TO_DROP)
               .replace(recoded)
               .assign(model_format=lambda x: pd.Categorical(x['model_format']),
                       reporting_guidelines_mention=lambda x: 
                           pd.Categorical(x['reporting_guidelines_mention']),
                       covid=lambda x: pd.Categorical(x['covid']),
                       foss_sim=lambda x: pd.Categorical(x['foss_sim']),
                       item_type=lambda x: pd.Categorical(x['item_type']),
                       model_has_doi=lambda x: 
                           pd.Categorical(x['model_has_doi']),
                       orcid=lambda x: pd.Categorical(x['orcid']),
                       readme=lambda x: pd.Categorical(x['readme']),
                       link_to_paper=lambda x: 
                           pd.Categorical(x['link_to_paper']),
                       steps_run=lambda x: pd.Categorical(x['steps_run']),
                       formal_dep_mgt=lambda x: 
                           pd.Categorical(x['formal_dep_mgt']),
                       informal_dep_mgt=lambda x: 
                           pd.Categorical(x['informal_dep_mgt']),
                       evidence_testing=lambda x:
                           pd.Categorical(x['evidence_testing']),
                       downloadable=lambda x: 
                           pd.Categorical(x['downloadable']),
                       interactive_online=lambda x: 
                           pd.Categorical(x['interactive_online']))
            )
    return clean
        