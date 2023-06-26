import os
import shutil




def check_iappen():
    
    file = open('control','r+')
    position = file.read().find('iappen')
    file.seek(position-2)
    parameter = int(file.read(1))
    if parameter == 1:
        print('iappen parameter is 1')
    else:
        
        file.seek(position-2)
        file.write('1')
        
        
        print('iappen parameter has been change to 1')
        
