from ffield_generator.generalparameter import generalparameter
from ffield_generator.atomparameter import atomparameter
from ffield_generator.bondparameter import bondparameter
from ffield_generator.valenceparameter import valenceparameter
from ffield_generator.torsionparameter import torsionparameter
from ffield_generator.hydrogenbondparameter import hydrogenbondparameter
from ffield_generator.diagonalterm import diagonalterm
from ffield_generator.params_input import params_input
from ffield_generator.create_folder import create_folder


def assign_parameter(ffield_section, type, parameter, value):
    
    if int(ffield_section)==1:
            generalparameter(int(type),value)
    if int(ffield_section)==2:
            atomparameter(int(type),int(parameter),value)
    if int(ffield_section)==3:
            bondparameter(int(type),int(parameter),value)
    if int(ffield_section)==4:
            diagonalterm(int(type),int(parameter),value)
    if int(ffield_section)==5:
            valenceparameter(int(type),int(parameter),value)
    if int(ffield_section)==6:
            torsionparameter(int(type),int(parameter),value) 
    if int(ffield_section)==7:
            hydrogenbondparameter(int(type),int(parameter),value)
    if int(ffield_section)>7: 
            print('Error in defined parameter region')



