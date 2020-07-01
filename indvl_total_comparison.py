import os
import shutil


def file_comparison(number_of_samples, data_folder_name, indvl_error_folder_name):
    
    if os.path.exists(data_folder_name):
        print('Total error folder exists.')
        
        if os.path.exists(indvl_error_folder_name):
            print('Individual error folder exists.')
            
            for i in range(0, number_of_samples):
                parameter_file = data_folder_name+"/"+"parameters"+str(i)
                error_file = indvl_error_folder_name+"/"+"individual_error"+str(i)
                if (os.path.isfile(parameter_file) == False) and (os.path.isfile(error_file) == True):
                    os.remove(error_file)
                    

    
    
    
    

