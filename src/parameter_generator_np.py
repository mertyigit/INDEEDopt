"""Read the params file and gets the ffield parameters as input"""

from pyDOE import *
import numpy


def parameter_generator(parameters, cycle):
    try:
        length = len(parameters)
        parameters_a = defaultdict(list)


        hc = lhs(length, cycle, criterion='centermaximin')

        
        for j in range(0,cycle):
            for i in range(0,length):
           
                parameters_a[j].append((float(parameters[i][5])-float(parameters[i][4]))*hc[j][i]+float(parameters[i][4]))
        
            
    except IOError:
        pass
        
    return parameters_a
