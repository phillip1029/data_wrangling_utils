#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler


# In[ ]:


scale = StandardScaler()
max_scale = MinMaxScaler()


# In[ ]:


def composite_score(df, num_cols):
    """
    Usage: to create a composite score and rank from a group of numerical columns

    Args:
    df: input dataframe name
    num_cols: list of numerical columns to use for the composite score

    return:
    dataframe with two columns added: Composite_score and composite_rank_order
    """
    df2 =df.copy()
    df2[num_cols] = scale.fit_transform(df2[num_cols])
    df2['Composite_score'] = df2.sum(axis=1)
    df2['Composite_score'] = max_scale.fit_transform(df2[['Composite_score']]) 
    df2 = df2.sort_values(['Composite_score'],ascending=False)
#     df2['composite_rank_order'] = np.arange(1, len(df)+1)
#     df2['composite_rank_group'] = pd.qcut(df2['Composite_score'],n,labels=[str(i) for i in range(n, 0, -1)])
    return df2


# In[ ]:


from functools import wraps
from time import time

def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        print('func:%r  took: %2.4f sec' %           (f.__name__,  te-ts))
        return result
    return wrap

