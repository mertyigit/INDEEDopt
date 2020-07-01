def connectivity():
    """Getting connectivities"""
    try:
        number_of_structures = 0
    
        with open('geo') as f:
            for line in f:
                finded = line.find('BIOGRF')
                if finded != -1:
                    number_of_structures += 1
    
        connectivities = []
    
    
        try:
            file = open("geo","r+")
            description = []
            position_end = 0
            
            for i in range(0,number_of_structures):
                
                ### Get the structure names
                position = file.read().find('DESCRP')
                file.seek(position+position_end)
                description.append(file.readline().split())
                connectivities.append(description[i][1])
                file.seek(position_end)
                
                
                ### Calculates number of atoms in each structure
                position = file.read().find('FORMAT ATOM')
                file.seek(position + position_end)
                file.readline()
                position = file.tell()
                file.seek(position_end)
                position_conect = file.read().find('FORMAT CONECT') + position_end
                number_of_atoms = int((position_conect-position)/81)
                
                file.seek(position_conect)
                file.readline()
                position = file.tell()
                
                file.seek(position)
                
                ### Connectivities are stored
                for i in range(0,number_of_atoms):
                    connectivities.append(file.readline().split())
                
                position = file.tell()
                
                position_end = file.read().find('END')+position
                file.seek(position_end)
            
        finally:
            file.close()
    except IOError:
        pass
    
    return connectivities
