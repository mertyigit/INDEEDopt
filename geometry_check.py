from collections import defaultdict


def geometry_check(structure_name, bond_length):
        
    try:    
        number_of_structures = len(structure_name)
        np = 0
        non_physical = defaultdict(list)     
        
              
        for i in range(0, number_of_structures):
            np = 0
            structure = structure_name[i][1]
            num_of_bonds = len(bond_length[structure])
                
            for j in range(0, num_of_bonds):
                 if bond_length[structure][j][0] == 0:
                     if bond_length[structure][j][1] == 0:
                         if round(bond_length[structure][j][2], 4) == 0:
                             np = 1
            
            non_physical[structure].append(str(np))
    except IOError:
        pass
            
    return non_physical