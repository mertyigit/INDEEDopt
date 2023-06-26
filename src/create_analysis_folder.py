import os
import shutil


def create_analysis_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        
    shutil.copy('ffield', folder_name)
    shutil.copy('parameters', folder_name)

    
