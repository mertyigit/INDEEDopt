

def torsionparameter(type, parameter, value):
    """Assigns values to the torsion parameters part of the force field file."""
    
    try:
        file = open("ffield","r+")
        position = file.read().find("Nr of torsions")
        file.seek(position)
        file.readline()
        position = file.tell()

        try:
            
            position = position + (76*(type-1))
            position = position + 13
            position = position + (parameter-1)*9
            
            file.seek(position)
            file.write(value.rjust(8))
    
        finally:
            file.close()
    except IOError:
        pass
