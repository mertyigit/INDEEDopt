import os
import shutil


def create_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        os.chdir(folder_name)
        
    shutil.copy('ffield', folder_name)
    shutil.copy('geo', folder_name)
    shutil.copy('params', folder_name)
    shutil.copy('exe', folder_name)
    shutil.copy('control', folder_name)
    
