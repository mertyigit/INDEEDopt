

def bondparameter(type, parameter, value):
    """Assigns values to the bond parameters part of the force field file. The noe is the number of elements"""
    
    try:
        file = open("ffield","r+")
        position = file.read().find("Nr of bonds")
        file.seek(position)
        file.readline()
        file.readline()
        position = file.tell()

        try:
            
            position = position + (79*2*(type-1))
            
            if parameter%8==0:
                position = position + (parameter//8)*79
                
                position = position + (parameter%8-1)*9
            else:
                position = position + (parameter//8)*79
                position = position + 7
                position = position + (parameter%8-1)*9
            
            file.seek(position)
            file.write(value.rjust(8))
    
        finally:
            file.close()
    except IOError:
        pass
