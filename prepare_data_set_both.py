## Last Updated: Feb 15 2021 - to avoid output error in cases that the user assigns very large parameter ranges

import os
import shutil
from collections import defaultdict

def prepare_data_set_error(initial_file_number):
    folder_name = 'individual_errors'
    data_folder_name = 'total_errors'
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
    if not os.path.exists(data_folder_name):
        os.makedirs(data_folder_name)
        
    error = defaultdict(list)
        #rootdir = os.getcwd()

    j=initial_file_number
    for subdir in os.listdir(os.getcwd()):
        if subdir.startswith('ffield'): 
            ffield_folder_name = subdir
            j=j+1
            if os.path.exists(ffield_folder_name):
                os.chdir(ffield_folder_name)
                if (os.path.isfile("fort.99") == True):
                    file = open("fort.99","r")
                    file_length = len(file.readlines())
                    file.seek(0)
                    file.readline()
                    #second file.readline() is for MAc, no need for ACI
                    file.readline()
                    position = file.tell()
                    
                    try:
                        for i in range(0,file_length-2):
                           #Ffield value
                           file.seek(position+61)
                           try:
                               error[i].append(float(file.read(11)))
                           except ValueError:
                               error[i].append(99999999)
                       
                           #Quantum Chemical value
                           file.seek(position+73)
                           error[i].append(float(file.read(11)))
                       
                           #Weight of the training set element
                           file.seek(position+85)
                           error[i].append(float(file.read(11)))
                       
                           #Position to the beginning of next line
                           position = position + 121
                       
                           #A control subroutine to avoid empty spaces in fort.99
                           file.seek(position)
                           null = file.readline()
                           if (file.tell() - position == 121):
                               file.seek(position)
                           else:
                               position = file.tell()
                           
                    finally:
                        file.close()
                
                    # Individual error output subroutine
                    
                    number_of_training_element = len(error)
                    
                    file2 = open("individual_error","w+") 
                    file2.seek(0)
                    
                    try:    
                    
                        for i in range(0, number_of_training_element):    
                            total_error ="{:.2f}".format(((error[i][1]-error[i][0])/error[i][2])**2)
                            #total_error =(((error[i][1]-error[i][0])/error[i][2])**2)
                            file2.write(str(i).rjust(10)+str(error[i][0]).rjust(12)+str(error[i][1]).rjust(12)+str(error[i][2]).rjust(12)+str(total_error).rjust(40)+"\n")
                            
                    finally:
                        file2.close()
                    
                    shutil.copy('individual_error', '../'+folder_name+'/'+'individual_error'+ str(j))
                    
                    #total error subroutine   
                    if (os.path.isfile("parameters") == True):
                        shutil.copy('parameters', '../'+data_folder_name+'/'+'parameters'+ str(j))
                       
                           
                    if (os.path.isfile("parameters") == False):
                        print("Parameters file does not exist")
                        
                    os.chdir('..')
                else:
                    print("File does not exist.")
                    
                    #total error subroutine   
                    if (os.path.isfile("parameters") == True):
                        shutil.copy('parameters', '../'+data_folder_name+'/'+'parameters'+ str(j))
                       
                           
                    if (os.path.isfile("parameters") == False):
                        print("Parameters file does not exist")
                        
                    os.chdir('..')

                    
                    
                error.clear()
            if not os.path.exists(ffield_folder_name):
                print("ffield-"+str(j)+" does not exist.")

