import os
import shutil


def data_set(number_of_samples, data_folder_name):
    if not os.path.exists(data_folder_name):
        os.makedirs(data_folder_name)
    
    
    for i in range(0,number_of_samples):
        folder_name = 'ffield-'+ str(i)
        
        if (os.path.isdir(folder_name) == True):
            os.chdir(folder_name)
            
            
            if (os.path.isfile("parameters") == True):
                shutil.copy('parameters', '../'+data_folder_name+'/'+'parameters'+ str(i))
                       
                           
            if (os.path.isfile("parameters") == False):
                print("Parameters file does not exist")
        
        else:
            print("Folder does not exist")        
        os.chdir('..')
    
    
    
    

