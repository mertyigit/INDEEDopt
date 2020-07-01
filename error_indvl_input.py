"""Read the params file and gets the ffield parameters as input"""

from collections import defaultdict
import os

def error_indvl_input():
    try:
        if (os.path.isfile("fort.99") == True):
            file = open("fort.99","r")
            file_length = len(file.readlines())
            file.seek(0)
            file.readline()
            position = file.tell()
            error = defaultdict(list)
            
            try:
                for i in range(0,file_length-2):
                   #Ffield value
                   file.seek(position+61)
                   error[i].append(float(file.read(12)))
                   
                   #Quantum Chemical value
                   file.seek(position+73)
                   error[i].append(float(file.read(12)))
                   
                   #Weight of the training set element
                   file.seek(position+85)
                   error[i].append(float(file.read(12)))
                   
                   #Position to the beginning of next line
                   position = position + 121
                   
                   
                   file.seek(position)
                   null = file.readline()
                   if (file.tell() - position == 121):
                       file.seek(position)
                   else:
                       position = file.tell()
                   
            finally:
                file.close()
        else:
            print("File does not exist.")
    except IOError:
        pass
        
    return error