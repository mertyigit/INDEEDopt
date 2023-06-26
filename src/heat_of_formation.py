from collections import defaultdict

def heat_of_formation(structure_name):
    """Getting heat of formation values"""
    try:
        number_of_structures = len(structure_name)
        hof = defaultdict(list)

        try:
            file = open("fort.74","r+")
            
            for j in range(0,number_of_structures):
                
                structure = structure_name[j][1]
                
                file.seek(0)
                position = file.read().find(' '+structure+'     ')
                
                if position == -1:
                    print('Structure: '+structure+' was not found. Please check the structure names')
                    hof[structure].append('NA')
                    
                else:
                    file.seek(position)
                    hof[structure].append((file.readline().split())[-1])
        
        finally:
            file.close()
    except IOError:
        pass
    
    return hof
