## This code is updated on Feb 10 2021


import tensorflow as tf
import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow import keras
from tensorflow.keras import layers
from sklearn.metrics import r2_score
from scipy import stats
from sklearn import preprocessing
from tqdm import tqdm
from sklearn.preprocessing import StandardScaler
import math
from sklearn.preprocessing import MinMaxScaler
from tensorflow.keras.callbacks import TensorBoard
np.set_printoptions(suppress=True)   
import sys
## path to the python script for data generation
Path2script = "/Users/mertyigitsengul/Documents/python_packages/"
sys.path.append(Path2script)

import warnings
warnings.filterwarnings("ignore")

import ffield_generator
from ffield_generator.generate_training_folder import generate_training_folder
from ffield_generator.error_output import error_output_bf
from ffield_generator.remove_forts import remove_forts  
from ffield_generator.parameter import assign_parameter
from ffield_generator.params_input_train import params_input_train
from ffield_generator.params_output import params_output

def bruteforce(param_size, num_prop, file_name, best_value, scan_width, iterations):
    
    df_gold = pd.read_csv("dl-gold.csv")
    df_gold = df_gold.iloc[:, 0:num_prop]
    df_weight = pd.read_csv("dl-weight.csv")
    df_weight = df_weight.iloc[:, 0:num_prop]
    data = pd.read_csv(file_name)
    data_size = data.shape[0]
    
    
    properties = np.arange(0, num_prop)

    x = data.loc[:,data.columns[range(param_size)]]
    y = data.loc[:,data.columns[range(param_size, num_prop+param_size)]]

    x_train_ns, x_test_ns, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
    y_train_ns = y_train.values
    y_train_ns = y_train.astype("float64")
    y_test_ns = y_test.values

    scaler = StandardScaler()
    print(scaler.fit(x))
    x_train = scaler.fit_transform(x_train_ns)
    x_test = scaler.transform(x_test_ns)
    y_train = scaler.fit_transform(y_train_ns)
    y_test = scaler.transform(y_test_ns)
    y_train= y_train_ns
    y_test = y_test_ns
    
    from tensorflow.keras.models import model_from_json
    # load json and create model
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    model = model_from_json(loaded_model_json)
    # load weights into new model
    model.load_weights("model.h5")
    print("Loaded model from disk")
    
    
    boundaries = pd.DataFrame()
    boundaries = pd.read_csv(os.path.join(".", "params-ml"), sep='\s+', header=None)
    
    bp=pd.read_csv('best_point.dat', sep='\t', header=None)
    best_point = np.zeros(bp.shape[0]-1)
    for i in range(0, bp.shape[0]-1):
        best_point[i]=float(bp.iloc[i][0].split()[1])
    print("BEST ERROR: "+str(best_value))
    
    #best_point = pd.read_csv(os.path.join(".", "best_point.dat"), sep='\s+', header=None)
    #boundaries[4] = best_point - boundaries[3]
    #boundaries[5] = best_point + boundaries[3]
    boundaries[4] = best_point - best_point*scan_width
    boundaries[5] = best_point + best_point*scan_width
    nn=0
    
    def f(x):
        para = np.zeros((1, param_size))
        para[0] = x
        scaler.fit(x_train_ns)
        a = scaler.transform(para)
        points = model.predict(a)
        Y = sum(((df_gold.values[0][0:num_prop]-points.astype("float64")[0][0:num_prop])/df_weight.values[0][0:num_prop])**2)
        return Y
        
        

    
    def prepare_test_folder(nn, x000, param_size, test_folder_name):
        #test_folder = "tests"       
        #nn=nn+1
        import shutil
        generate_training_folder(test_folder_name)

        parameters = params_input_train()
        values=np.transpose(x000)
        os.chdir(test_folder_name)
        np.savetxt("dl-parameters-rndm-"+str(nn)+".dat", np.transpose(x000), fmt='%f')
        
        file = open('params-ml','w')
        file.seek(0)
        for j in range(0, boundaries.shape[0]):
            file.write(str(boundaries.values[j][0].astype(int))
                        +"  "+str(boundaries.values[j][1].astype(int))
                        +"  "+str(boundaries.values[j][2].astype(int))
                        +"  "+str(boundaries.values[j][3])
                        +"  "+str(np.transpose(x000)[j])
                        +"  "+str(np.transpose(x000)[j])+"\n")
        
        file.close()
        
        for i in range(0,param_size):
            value = str("{:.4f}".format(values[i]))
            assign_parameter(parameters[i][0], parameters[i][1], parameters[i][2], value)
            params_output(parameters[i][0],parameters[i][1],parameters[i][2], value)
        
        os.system('./exe')
    
        reaxff_error = error_output_bf(param_size, "dl-parameters-rndm-"+str(nn)+".dat")
        
        remove_forts()
        
        os.chdir('..')
        print("ReaxFF Error: "+ str(reaxff_error))
        file = open('ReaxFF-error','a+')
        file.write(str(reaxff_error)+'\n')
        file.close()
        return reaxff_error
        
        
    import subprocess
    import time
    
    pbar = tqdm(total=iterations)

    #best_points = np.zeros((num_cores, param_size))
    #best_value=f(best_point[0])

    #scaler.fit(y_train_ns)
    #gold = scaler.transform(df_gold.values)
    #weight = 1
    scaler.fit(x_train_ns)
    for i in range(0, iterations):
        np.random.RandomState()
        b=np.random.rand(1, param_size)
        c = ((b*(boundaries[5]-boundaries[4]).values)+boundaries[4].values)
        a = scaler.transform(c)
        points = model.predict(a)
    
        r2 = sum(((df_gold.values[0][0:num_prop]-points.astype("float64")[0][0:num_prop])/df_weight.values[0][0:num_prop])**2)
        #r2 = sum(((gold[0]-points.astype("float64")[0][0:num_prop])/weight)**2)
    
        pbar.update()
        if r2<best_value:
            test_folder_name = 'test-'+ str(nn)
            reaxff_error = prepare_test_folder(nn, c[0], param_size, test_folder_name)
            if float(reaxff_error) < best_value:
                best_value=float(reaxff_error)
                best_point=c
            else:
                os.system('rm -r '+test_folder_name)
                
            print("BEST VALUE: "+str(best_value))
            print("BEST POINT: "+str(best_point))
            nn = nn + 1
            
            #best_value = r2
            #best_point = c
            #print(best_value)
            #print(best_point)
            #np.savetxt("dl-parameters-rndm-"+str(nn)+".dat", np.transpose(best_point), fmt='%f')
            
            
            
    pbar.close() 
    print(best_value)
    
    
    return best_value
    
    
