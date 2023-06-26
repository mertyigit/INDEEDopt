

def structure_name():
    """Getting coordinates"""
    try:
        number_of_structures = 0
    
        with open('fort.90') as f:
            for line in f:
                finded = line.find('BIOGRF')
                if finded != -1:
                    number_of_structures += 1    
        f.close()
        try:
            file = open("fort.90","r+")
            description = []
            position_end = 0
            
            for i in range(0,number_of_structures):
                
                position = file.read().find('DESCRP')
                file.seek(position+position_end)
                description.append(file.readline().split())
                
                position_end = file.tell()
                file.seek(position_end)
            
        finally:
            file.close()
    except IOError:
        pass
    
    return description
