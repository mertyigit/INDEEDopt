import os
import shutil


def generate_training_folder_v1(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    shutil.copy('ffield', folder_name)
    shutil.copy('geo', folder_name)
    #shutil.copy('params', folder_name)
    shutil.copy('params-ml', folder_name)
    shutil.copy('exe', folder_name)
    shutil.copy('control', folder_name)
    shutil.copy('trainset.in', folder_name)
    
    os.chdir(folder_name)
    file = open('iopt','w+')
    file.seek(0)
    file.write('0'.rjust(3))
    os.chdir('..')
    
def generate_training_folder(folder_name):
    #if not os.path.exists(folder_name):
    #    os.makedirs(folder_name)
    #    
    #shutil.copy('ffield', folder_name)
    #shutil.copy('geo', folder_name)
    ##shutil.copy('params', folder_name)
    #shutil.copy('params-ml', folder_name)
    #shutil.copy('exe', folder_name)
    #shutil.copy('control', folder_name)
    #shutil.copy('trainset.in', folder_name)
    
    if not os.path.exists(folder_name):
        shutil.copytree('folder', folder_name)
    
    os.chdir(folder_name)
    file = open('iopt','w+')
    file.seek(0)
    file.write('0'.rjust(3))
    os.chdir('..')