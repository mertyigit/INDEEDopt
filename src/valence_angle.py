from collections import defaultdict
import math


def valence_angle(coordinate, bond_lengths, structure_name):
    try:
        number_of_structures = len(structure_name)
        valence = defaultdict(list)
        
        
        for k in range(0, number_of_structures):
            
            structure = structure_name[k][1]
            number_of_atoms = len(coordinate[structure])
            number_of_bonds = len(bond_lengths[structure])
            index = 1
            
            
            if number_of_bonds > 1:
                for i in range(0, number_of_bonds):
                    atom_middle = bond_lengths[structure][i][0]
                    atom_1 = bond_lengths[structure][i][1]
                    a = float(bond_lengths[structure][i][2])
                    j = i+1
                    
                    
                    while j < number_of_bonds:
                        if bond_lengths[structure][j][0] == atom_middle:
                            
                            atom_2 = bond_lengths[structure][j][1]
                            b = float(bond_lengths[structure][j][2])
                            
                            delx = float(coordinate[structure][atom_1-1][3]) - float(coordinate[structure][atom_2-1][3])
                            dely = float(coordinate[structure][atom_1-1][4]) - float(coordinate[structure][atom_2-1][4])
                            delz = float(coordinate[structure][atom_1-1][5]) - float(coordinate[structure][atom_2-1][5])
                            
                            c = ((delx**2)+(dely**2)+(delz**2))**0.5
                            
                            valence_angle = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
                            
                            valence[structure].append([atom_1, atom_middle, atom_2, valence_angle])
                            
                            j += 1
                        else:
                            j +=1
                for i in range(0, number_of_bonds):
                    atom_middle = bond_lengths[structure][i][1]
                    atom_1 = bond_lengths[structure][i][0]
                    a = float(bond_lengths[structure][i][2])
                    j = i+1
                    
                    
                    while j < number_of_bonds:
                        if bond_lengths[structure][j][0] == atom_middle:
                            
                            atom_2 = bond_lengths[structure][j][1]
                            b = float(bond_lengths[structure][j][2])
                            
                            delx = float(coordinate[structure][atom_1-1][3]) - float(coordinate[structure][atom_2-1][3])
                            dely = float(coordinate[structure][atom_1-1][4]) - float(coordinate[structure][atom_2-1][4])
                            delz = float(coordinate[structure][atom_1-1][5]) - float(coordinate[structure][atom_2-1][5])
                            
                            c = ((delx**2)+(dely**2)+(delz**2))**0.5
                            
                            valence_angle = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
                            
                            valence[structure].append([atom_1, atom_middle, atom_2, valence_angle])
                            
                            j += 1
                        else:
                            j +=1
                for i in range(0, number_of_bonds):
                    atom_middle = bond_lengths[structure][i][1]
                    atom_1 = bond_lengths[structure][i][0]
                    a = float(bond_lengths[structure][i][2])
                    j = i+1
                    
                    
                    while j < number_of_bonds:
                        if bond_lengths[structure][j][1] == atom_middle:
                            
                            atom_2 = bond_lengths[structure][j][0]
                            b = float(bond_lengths[structure][j][2])
                            
                            delx = float(coordinate[structure][atom_1-1][3]) - float(coordinate[structure][atom_2-1][3])
                            dely = float(coordinate[structure][atom_1-1][4]) - float(coordinate[structure][atom_2-1][4])
                            delz = float(coordinate[structure][atom_1-1][5]) - float(coordinate[structure][atom_2-1][5])
                            
                            c = ((delx**2)+(dely**2)+(delz**2))**0.5
                            
                            valence_angle = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
                            
                            valence[structure].append([atom_1, atom_middle, atom_2, valence_angle])
                            
                            j += 1
                        else:
                            j +=1
                for i in range(0, number_of_bonds):
                    atom_middle = bond_lengths[structure][i][0]
                    atom_1 = bond_lengths[structure][i][1]
                    a = float(bond_lengths[structure][i][2])
                    j = i+1
                    
                    
                    while j < number_of_bonds:
                        if bond_lengths[structure][j][1] == atom_middle:
                            
                            atom_2 = bond_lengths[structure][j][0]
                            b = float(bond_lengths[structure][j][2])
                            
                            delx = float(coordinate[structure][atom_1-1][3]) - float(coordinate[structure][atom_2-1][3])
                            dely = float(coordinate[structure][atom_1-1][4]) - float(coordinate[structure][atom_2-1][4])
                            delz = float(coordinate[structure][atom_1-1][5]) - float(coordinate[structure][atom_2-1][5])
                            
                            c = ((delx**2)+(dely**2)+(delz**2))**0.5
                            
                            valence_angle = math.degrees(math.acos((a**2+b**2-c**2)/(2*a*b)))
                            
                            valence[structure].append([atom_1, atom_middle, atom_2, valence_angle])
                            
                            j += 1
                        else:
                            j +=1
                                                                 
    except IOError:
        pass
    
    return valence
