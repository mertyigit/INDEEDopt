## Modified on Fevb 15 2021- 1.50pm

import sys
## path to the python script for data generation
Path2script = "/Users/mertyigitsengul/Documents/python_packages/INDEEDopt_code/"
sys.path.append(Path2script)

import warnings
warnings.filterwarnings("ignore")

import ffield_generator
from ffield_generator.parameter import assign_parameter
from ffield_generator.params_input_train import params_input_train
from ffield_generator.create_folder import create_folder
from ffield_generator.params_output import params_output
from ffield_generator.error_output import error_output
from ffield_generator.parameter_generator import parameter_generator
from ffield_generator.generate_training_folder import generate_training_folder
from ffield_generator.remove_files import remove_files
from ffield_generator.geometry_check import geometry_check
from ffield_generator.check_iappen import check_iappen
from ffield_generator.prepare_data_set_both import prepare_data_set_error
from ffield_generator.data_extract import data_extract
from ffield_generator.data_extract3 import data_extract3
from ffield_generator.local_data_generator2 import local_data_generator
from ffield_generator.best_error_print import best_error_print
from ffield_generator.dl2 import dl2
from ffield_generator.remove_forts import remove_forts
from ffield_generator.bruteforce2 import bruteforce
from ffield_generator.generalparameter_read import generalparameter_read
from ffield_generator.atomparameter_read import atomparameter_read
from ffield_generator.bondparameter_read import bondparameter_read
from ffield_generator.valenceparameter_read import valenceparameter_read
from ffield_generator.torsionparameter_read import torsionparameter_read
from ffield_generator.hydrogenbondparameter_read import hydrogenbondparameter_read
from ffield_generator.diagonalterm_read import diagonalterm_read
from ffield_generator.read_parameter import read_parameter
from ffield_generator.define_ranges import define_ranges


import shutil

from pyDOE import *
from collections import defaultdict
import os
import random
import time
import pandas as pd


#Parallel part
from joblib import Parallel, delayed
import multiprocessing
from multiprocessing.dummy import Pool
from scoop import futures
t0 = time.time()

## if gpf value is zero, then the parameter ranges in params-ml file is used.
## if gpf value is more than zero, the value is used as a percentage value and define parameter ranges using this value

gpf = 5



## number of samples to be taken in the parameter space
## nos is the first scan of parameter space
nos = 4
## nos_2 is the second scan around the best of the point
nos_2 = 10


#number of properties in training set
num_prop = 96

#number of iterations to go deep into local minima

lm_iter = 2

## For now, it should be taken as 1. Normally, it selects the best points on each parameter space scan and concentrate of around them.
bn = 1


shutil.copy('folder/ffield', '.')

cycle = range(nos)
parameters = params_input_train()

#if gpf > 0:
#    print("Generating parameter ranges")
#    #os.remove('params-ml')
#    define_ranges(parameters, gpf)
#
#shutil.copy('params-ml', 'folder/')
#
#values = parameter_generator(parameters, len(cycle))
length = len(parameters)


def func(values, j):
    
    #taking the information about which parameters will be altered
    
    #file = open("values"+str(j),"a+")
    #file.write(str(values[j]) + "\n")
    #file.close()

    
    try:
        
        ### Generate folder, enter to the folder, assign parameter values, start executable, leave ###
           
        folder_name = 'ffield-'+ str(j)
        generate_training_folder(folder_name)
        
        os.chdir(folder_name)
        for i in range(0,length):
            value = str("{:.4f}".format(values[j][i]))
            assign_parameter(parameters[i][0], parameters[i][1], parameters[i][2], value)
            params_output(parameters[i][0],parameters[i][1],parameters[i][2], value)
        
        os.system('./exe')
        

        error_output(length)
        
        remove_forts()

        
        os.chdir('..')
        
    except:
        pass

def data_set(initial_file_number):
    if os.path.exists('ffield'):
        os.remove('ffield')
    prepare_data_set_error(initial_file_number)

def zipping(iter):
    print("zipping in progress")
    os.system('tar -cvzf errors'+str(iter)+'.tar individual_errors/ total_errors')
    
def clean_fold():
    os.system('rm -r ffield-*')

def data_ext(nos, length, num_prop):
    data_extract(nos, length, num_prop)

def data_ext3(ifn, length, num_prop, nos_2, file_name):
    data_extract3(ifn, length, num_prop, nos_2, file_name)

    
def ldg(width, length, bn):
    params = np.zeros((bn, length,6))
    params = local_data_generator(width, length, bn)
    return params
    
def valuess(iter, params, cycle):
    values = parameter_generator(params[iter], len(cycle))
    return values
        
def doneElement(inFuture):
    print("Done: {}".format(inFuture.result()))

def run(values):
    # Create launches
    launches = [futures.submit(func ,values, j) for j in cycle]

    # Add a callback on every launches
    for launch in launches:
        launch.add_done_callback(doneElement)
    
    # Wait for the launches to complete.
    [completed for completed in futures.as_completed(launches)]
    
    

if __name__ == '__main__':
    
    enough = 0
    iterating = 0
    
    if gpf > 0:
        print("Generating parameter ranges")
        #os.remove('params-ml')
        define_ranges(parameters, gpf)
    
    shutil.copy('params-ml', 'folder/')
    
    values = parameter_generator(parameters, len(cycle))
    
    
    while enough == 0:
        if iterating == 0:
            for i in range(0, lm_iter):
                print("ITERATION: "+str(i))
                if i==0:
                    initial_file_number=-1
                    run(values)
                    data_set(initial_file_number)
                    #zipping(0)
                    clean_fold()
                    data_ext(nos, length, num_prop)
                    
                    
                else:
                    print("generating parameters")
                    params = ldg(lm_iter-i, length, bn)
                    cycle=range(nos_2)
                    
                    for k in range(0, bn):
                        ifn = (i-1)*(bn*nos_2)+(k*nos_2)+(nos-1)
                        values = valuess(k, params, cycle)
                        
                        #file = open("values","a+")
                        #file.write(str(values) + "\n")
                        #file.close()
                        
                        
                        shutil.copy('folder/ffield', '.')
                        run(values)
                        data_set(ifn)
                        clean_fold()
                        data_ext3(ifn, length, num_prop, nos_2, 'dl-data-l.csv')
                        best_error_print(length, bn)
                    #zipping(i)
        if iterating == 1:
            
            cycle=range(nos_2)
            
            lm_iter=lm_iter+1
            i = i+1
            params = ldg(lm_iter-i, length, bn)
            
            for l in range(0, bn):
                ifn = (i-1)*(bn*nos_2)+(k*nos_2)+(nos-1)
                values = valuess(l, params, cycle)
                
                #file = open("values","a+")
                #file.write(str(values) + "\n")
                #file.close()
                
                
                shutil.copy('folder/ffield', '.')
                run(values)
                data_set(ifn)
                #zipping(i)
                clean_fold()
                data_ext3(ifn, length, num_prop, nos_2, 'dl-data-l.csv')
                best_error = best_error_print(length, bn)
                                
        
        iterating = 1
        #data_ext(ifn, length, num_prop)
        accuracy = dl2(length, num_prop, 'dl-data-l.csv' )
        print("Accuracy: "+str(accuracy))  
        accuracy=pd.read_csv('accuracy.dat', sep='\t', header=None)
        print(accuracy)
        if accuracy.shape[0]>2:
            accuracy_change=100*abs(accuracy[0][accuracy.shape[0]-1]-accuracy[0][accuracy.shape[0]-2])/accuracy[0][accuracy.shape[0]-2]
            if accuracy_change < 2:
                enough = 1
    
    zipping(1)
    
    # STARTING BRUTE FORCE
    print("STARTING BRUTE FORCE ALGORITHM")
    bruteforce(length, num_prop, 'dl-data-l.csv', best_error, 0.05, 10000000)


t1 = time.time()


total = t1-t0
print('Total Time (hours): ' + str(total/3600))
