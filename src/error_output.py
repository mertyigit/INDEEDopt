
def error_output(number_of_parameters):
    
    """Write the optimized error values into the params file near the corresponding parameter identicator"""
    
    try:
        
        file2 = open("parameters", "r+")
        file2.seek(0)
        position2 = file2.tell()
        
        file = open("fort.13","r")        
        file.seek(0)
        position = file.tell()
        
        try:
            
            file.seek(0)
            error = file.read(12)
            
            file2.seek(20)
            file2.write("  " + error.rjust(18))
        
        finally:
            file.close()
    except IOError:
        pass

def error_output_bf(number_of_parameters, parameters_file_name):
    
    """Write the optimized error values into the params file near the corresponding parameter identicator"""
    
    try:
        
        file2 = open(parameters_file_name, "a+")
        #file2.seek(0)
        #position2 = file2.tell()
        
        file = open("fort.13","r")        
        file.seek(0)
        position = file.tell()
        
        try:
            
            file.seek(0)
            error_bf = file.read(12)
            
            #file2.seek(20)
            file2.write("\n TOTAL ERROR: " + error_bf.rjust(18))
        
        finally:
            file.close()
    except IOError:
        pass
    return error_bf