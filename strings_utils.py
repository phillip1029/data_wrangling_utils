
from fuzzy_match import match
from fuzzy_match import algorithims

import pandas as pd 
import numpy as np

def fuzzy_matching(df1, col1, df2, col2):
    """
    Usage: matching two dataframes by columns with spelling variations
    Developer: Phillip Peng (phillip.peng@mail.waldenu.edu)   
    """
    
    def matching(x):      
        return match.extractOne(x, df2[col2].tolist())
    
    df1['matched_results'] = df1[col1].apply(matching) 
    
    matched_results = pd.DataFrame(df1['matched_results'].tolist())    
    matched_results.columns = [col2 +'_matched', 'matched_prob'] 
    
    df_matched = pd.concat([df1.reset_index(drop=True), matched_results.reset_index(drop=True)], axis=1)
    df_matched = df_matched.drop(columns=['matched_results'])    
    df_matched = df_matched.merge(df2, how='left', left_on=col2 +'_matched', right_on = col2)
    
    return df_matched


#  df_matched = fuzzy_matching(df1, 'Program Name', df2, "program_name")

 




