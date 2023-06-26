import os
import pandas as pd
import numpy as np
import math
import shutil
from ffield_generator.read_parameter import read_parameter



def define_ranges(parameters, percentage):
    percentage=float(percentage)/100
    file=open("params-ml","w")
    for i in range(0, len(parameters)):
        value=float(read_parameter(parameters[i][0], parameters[i][1], parameters[i][2]))        
        file.write(parameters[i][0].rjust(8)
                   + parameters[i][1].rjust(8)
                   + parameters[i][2].rjust(8)
                   + parameters[i][3].rjust(8)
                   + str("{:.2f}".format(value-value*percentage)).rjust(8)
                   + str("{:.2f}".format(value+value*percentage)).rjust(8)
                   + '\n'
                  )
    file.close()



