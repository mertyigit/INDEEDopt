import os
import shutil
from collections import defaultdict
import os
import pandas as pd
import numpy as np

def best_error_print(length, bn):
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
    print("SORTED ERRORS")
    print(sortedd)
    boundaries = pd.DataFrame()
    boundaries = pd.read_csv(os.path.join('.', "params-ml"), sep='\s+', header=None)
    if not os.path.exists('params-ml'):
        print('params-ml file cannot be found')
    
    print("Best "+str(bn)+" error values: ")
    
    for i in range(0, bn):
        print(sortedd.loc[:, 'error'].iloc[i])
        file = open("best_error_values.dat","a+")
        file.write(str(sortedd.loc[:, 'error'].iloc[i]) + "\n")
        file.close()
        

    print("best error value: ")
    print(sortedd.loc[:, 'error'].iloc[0])
    file = open("best_error.dat","a+")
    file.write(str(sortedd.loc[:, 'error'].iloc[0]) + "\n")
    file.close()
    pd.set_option('display.max_rows', 1000)
    print("best point: ")
    print((sortedd.loc[:, ['parameter-{}'.format(i) for i in range(0,sortedd.shape[1]-2)]].iloc[0]))
    file = open("best_point.dat","w+")
    file.write(str((sortedd.loc[:, ['parameter-{}'.format(i) for i in range(0,sortedd.shape[1]-2)]].iloc[0])) + "\n")
    file.close()
    

    return sortedd.loc[:, 'error'].iloc[0]
    
