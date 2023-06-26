from ffield_generator.generalparameter_read import generalparameter_read
from ffield_generator.atomparameter_read import atomparameter_read
from ffield_generator.bondparameter_read import bondparameter_read
from ffield_generator.valenceparameter_read import valenceparameter_read
from ffield_generator.torsionparameter_read import torsionparameter_read
from ffield_generator.hydrogenbondparameter_read import hydrogenbondparameter_read
from ffield_generator.diagonalterm_read import diagonalterm_read
from ffield_generator.params_input import params_input
from ffield_generator.create_folder import create_folder


def read_parameter(ffield_section, type, parameter):
    
    if int(ffield_section)==1:
            value=generalparameter_read(int(type))
    if int(ffield_section)==2:
            value=atomparameter_read(int(type),int(parameter))
    if int(ffield_section)==3:
            value=bondparameter_read(int(type),int(parameter))
    if int(ffield_section)==4:
            value=diagonalterm_read(int(type),int(parameter))
    if int(ffield_section)==5:
            value=valenceparameter_read(int(type),int(parameter))
    if int(ffield_section)==6:
            value=torsionparameter_read(int(type),int(parameter)) 
    if int(ffield_section)==7:
            value=hydrogenbondparameter_read(int(type),int(parameter))
    if int(ffield_section)>7: 
            print('Error in defined parameter region')
            
    return value



