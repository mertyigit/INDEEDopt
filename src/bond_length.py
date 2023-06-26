from collections import defaultdict
from itertools import combinations


def bond_length(coordinate, connectivity, structure_name):
    """Getting coordinates"""
    try:
        
        number_of_structures = len(structure_name)
        
        bond_lengths = defaultdict(list)

            
        for i in range(0, number_of_structures):
            
            connectivity_list_d = []
            connectivity_list_nd = []

            structure = structure_name[i][1]
            number_of_atoms = len(connectivity[structure])
            if len(connectivity[structure]) > 1:
                for j in range(0, number_of_atoms):
                    if len(connectivity[structure][j]) > 2:
                        atom_1 = connectivity[structure][j][1]
                        atom_2 = connectivity[structure][j][2]
                        if atom_2 > atom_1:
                            connectivity_list_d.append((atom_1, atom_2))
                        if atom_1 > atom_2:
                            connectivity_list_d.append((atom_2, atom_1))
                    else:
                        connectivity_list_d.append((0, 0))
                connectivity_list_nd = list(set(connectivity_list_d))
                
                for k in range(0, len(connectivity_list_nd)):
                    
                    atom_1 = int(connectivity_list_nd[k][0])
                    atom_2 = int(connectivity_list_nd[k][1])
                    
                    delx = float(coordinate[structure][atom_1-1][3]) - float(coordinate[structure][atom_2-1][3])
                    dely = float(coordinate[structure][atom_1-1][4]) - float(coordinate[structure][atom_2-1][4])
                    delz = float(coordinate[structure][atom_1-1][5]) - float(coordinate[structure][atom_2-1][5])
              
                    bond_length = ((delx**2)+(dely**2)+(delz**2))**0.5
                    bond_lengths[structure].append([atom_1, atom_2, bond_length])
            
           
    except (IOError, ValueError) as error:
        pass
    
    return bond_lengths
