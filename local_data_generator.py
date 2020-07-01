import os
import shutil
from collections import defaultdict
import os
import pandas as pd
import numpy as np

def local_data_generator(width, length):
    target_dir = "total_errors/"
    if not os.path.exists(target_dir):
        print('total_errors folder cannot be found')
    file_list = os.listdir(target_dir)
    df_list = pd.DataFrame()
    for file in sorted(file_list, key=lambda a: int(a.split("s")[1])):
        df = pd.read_csv(os.path.join(target_dir, file), sep='\s+', header=None)
        df = df.T
        df = df.add_prefix('parameter-')
        df = df.drop([0, 1, 2])
        if df.shape[0] > 1:
            if df['parameter-0'][4] == '************':
                df['error'] = np.nan
                df['feasibility'] = 0
                df =  df.drop([4])
            else:
                df['error'] = df['parameter-0'][4]
                df['feasibility'] = 1
                df =  df.drop([4])
        else:
            df['error'] = np.nan
        df_list = df_list.append(df)
    df_list.index = range(len(df_list))
    
    
    df_list.index = range(len(df_list))
    sortedd = df_list.sort_values('error')
    print(sortedd)
    boundaries = pd.DataFrame()
    boundaries = pd.read_csv(os.path.join('.', "params-ml"), sep='\s+', header=None)
    if not os.path.exists('params-ml'):
        print('params-ml file cannot be found')
    
    params = np.zeros((length,6))
    params[:,0]=boundaries[0]
    params[:,1]=boundaries[1]
    params[:,2]=boundaries[2]
    params[:,3]=boundaries[3]
    params[:,4]=sortedd.iloc[0][2:sortedd.shape[1]]-boundaries[3].values*width
    params[:,5]=sortedd.iloc[0][2:sortedd.shape[1]]+boundaries[3].values*width

    print("best error value: ")
    print(sortedd.iloc[0][0])
    file = open("best_errors.dat","a+")
    file.write(str(sortedd.iloc[0][0]) + "\n")
    file.close()

    return params
    
