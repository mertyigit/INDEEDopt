def params_output(section, type, parameter, value):
    
    """Write the assigned parameter values into the params file near the corresponding parameter identicator"""
    
    try:
        file = open("parameters","a+")        
        file.seek(0)
        length=5
        try:
            file.write(section.rjust(2) + "  " + type.rjust(2) + "  " + parameter.rjust(2) + "  " + value.rjust(8) + "                    \n")
        
        finally:
            file.close()
    except IOError:
        pass
