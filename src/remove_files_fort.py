import os
import shutil

def remove_files(structure_name, folder_name, non_physical):
    
    try:
        os.chdir(folder_name)
        
        
        number_of_structures = len(structure_name)
        
        for i in range(0, number_of_structures):
            
            structure = structure_name[i][1]
            
            if int(non_physical[structure][0]) == 1:
                if os.path.exists(structure):
                    os.remove(structure)
        os.chdir('..')
            
                
    except IOError:
            pass
    
