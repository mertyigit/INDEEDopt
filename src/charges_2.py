from collections import defaultdict

def charges(structure_name):
    """Getting charges"""
    try:
        number_of_structures = len(structure_name)
        charges = defaultdict(list)

        try:
            file = open("fort.7","r+")
            
            for j in range(0,number_of_structures):
                
                structure = structure_name[j][1]
                
                file.seek(0)
                position_1 = file.read().find(' '+structure+'     ')
                file.seek(position_1+20)
                position_2 = file.read().find(' '+structure+'     ')
                
                position = position_1 + 20 + position_2
                if position == -1:
                    print('Structure: '+structure+' was not found. Please check the structure names')
                    charges[structure].append('NA')
                    
                else:
                    file.seek(position-4)
                    number_of_atoms = int(file.readline().split()[0])
                    
                    
                    for i in range(0, number_of_atoms):
                        charges[structure].append([i+1, (file.readline().split())[-1]])
                    
                    
        finally:
            file.close()
    except IOError:
        pass
    
    return charges
