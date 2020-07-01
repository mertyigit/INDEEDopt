
def atomparameter(type, parameter,value):
    """Assigns values to the atom parameters part of the force field file. The noe is the number of elements"""
    
    try:
        file = open("ffield","r+")
        position = file.read().find("Nr of atoms")
        file.seek(position)
        file.readline()
        file.readline()
        file.readline()
        file.readline()
        position = file.tell()
    
        try:
            position = position + (76*4*(type-1))
            position = position + 1
            file.seek(position)
            position = position - 1
            if parameter%8==0:
                position = position + (parameter//8)*76
                
                position = position + (parameter%8-1)*9
            else:
                position = position + (parameter//8)*76
                position = position + 4
                position = position + (parameter%8-1)*9
            
            file.seek(position)
            file.write(value.rjust(8))

        finally:
            file.close()
    except IOError:
        pass
