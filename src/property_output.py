def property_output(structure_name, bond_length, valence_angle, charges, heat_of_formation):
    
    """Write the molecular property values into a file"""
    
    try:
        file = open("property","a+")        
        file.seek(0)
        
        number_of_structures = len(structure_name)
        
        try:
            
            for i in range(0, number_of_structures):
                
                structure = structure_name[i][1]
                file.write(structure+"\n")
                
                file.write('GEOMETRY\n')
                num_of_bonds = len(bond_length[structure])
                
                for j in range(0, num_of_bonds):
                    atom_b1 = str(bond_length[structure][j][0])
                    atom_b2 = str(bond_length[structure][j][1])
                    bond = str(round(bond_length[structure][j][2], 4))
                    file.write(atom_b1.rjust(6)+atom_b2.rjust(6)+bond.rjust(20)+"\n")
                
                num_of_angles = len(valence_angle[structure])
                
                for j in range(0, num_of_angles):
                    atom_a1 = str(valence_angle[structure][j][0])
                    atom_a2 = str(valence_angle[structure][j][1])
                    atom_a3 = str(valence_angle[structure][j][2])
                    angle = str(round(valence_angle[structure][j][3], 4))
                    file.write(atom_a1.rjust(6)+atom_a2.rjust(6)+atom_a3.rjust(6)+angle.rjust(14)+"\n")
                
                file.write('ENDGEOMETRY\n')
                
                file.write('CHARGES\n')
                num_of_atoms = len(charges[structure])
                
                for j in range(0, num_of_atoms):
                    atom_c1 = str(charges[structure][j][0])
                    charge = charges[structure][j][1]
                    file.write(atom_c1.rjust(6)+charge.rjust(10)+"\n")
                
                file.write('ENDCHARGES\n')
                
                file.write('HEATFO\n')
                
                heatfo = heat_of_formation[structure][0]
                file.write(heatfo.rjust(10)+"\n")
                
                file.write('ENDHEATFO\n')
                
        finally:
            file.close()
    except IOError:
        pass