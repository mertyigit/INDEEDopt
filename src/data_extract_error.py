import os
import pandas as pd
import numpy as np
import math


def data_extract(data_size, param_size, prop_size):
    properties = np.arange(0, prop_size)
    num_prop = len(properties)
    
    target_dir = "total_errors/"
    error_dir = "individual_errors/"
    train_dir = "."

    file_list = os.listdir(target_dir)
    file_list_e = os.listdir(error_dir)
    file_list_b = os.listdir(train_dir)
    
    df_list = pd.DataFrame()
    for file in sorted(file_list, key=lambda a: int(a.split("s")[1])):
        df = pd.read_csv(os.path.join(target_dir, file), sep='\s+', header=None)
        name = file[len(file.rstrip('0123456789')):]
        df = df.drop(columns=[0, 1, 2])
        df = df.T
        df_list[name] = df.iloc[0]
    df_list = df_list.T
    df_list = df_list.add_prefix('parameter-')
    
    file_list_e = os.listdir(error_dir)
    a = np.empty(data_size)
    a[:] = np.nan
    df_error = pd.DataFrame({'sample': a})
    for i in range(0, num_prop):
        df_error['property-'+str(i)] = a
    for file in file_list_e:
        df_e = pd.read_csv(os.path.join(error_dir, file), sep='\s+', header=None)
        name_e = file[len(file.rstrip('0123456789')):]
        df_error.at[int(name_e),'sample'] = int(name_e)
        for j in range(0, num_prop):
            df_error.at[int(name_e),'property-'+str(j)] = df_e.loc[properties[j]][4]
            
    df_gold = pd.DataFrame()
    df_weight = pd.DataFrame()
    for i in range(0, num_prop):
        df_gold['property-'+str(i)] = 0
        df_weight['property-'+str(i)] = 0
    for j in range(0, num_prop):
        df_gold.at[0,'property-'+str(j)] = df_e.loc[properties[j]][2]
        df_weight.at[0, 'property-'+str(j)] = df_e.loc[properties[j]][3]
        
    data = pd.DataFrame(index=[str(j) for j in range(param_size)], columns=['parameter-'+str(i) for i in range(param_size)])
    for i in range(0, num_prop):
        data['property-'+str(i)] = np.nan
    for i in range(0, data_size):
        for j in range(0, num_prop):
            data.at[str(i), 'property-'+str(j)] = df_error['property-'+str(j)][i]
        for j in range(0, param_size):
            data.at[str(i), 'parameter-'+str(j)]=df_list.loc[str(i)][j]
    data = data.dropna(axis=0, how='any')
    
    data.to_csv(path_or_buf="dl-data.csv", index=False)
    df_gold.to_csv(path_or_buf="dl-gold.csv", index=False)
    df_weight.to_csv(path_or_buf="dl-weight.csv", index=False)

    
