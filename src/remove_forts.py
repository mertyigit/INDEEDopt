import os
import pandas as pd
import numpy as np
from tqdm import tqdm

import math
from time import time
np.set_printoptions(suppress=True)    


def remove_forts():
    """this part is to remove the unneccessary files at the end of the simulation. Our purpose is to combine this part with the start of machine learning part in the future."""
    if os.path.exists('ffieldss'):
        os.remove('ffieldss')
    if os.path.exists('control'):
        os.remove('control')
    if os.path.exists('exe'):
        os.remove('exe')
    if os.path.exists('geo'):
        os.remove('geo')
    if os.path.exists('iopt'):
        os.remove('iopt')    
    if os.path.exists('summary.txt'):
        os.remove('summary.txt')    
    if os.path.exists('run.log'):
        os.remove('run.log')    
    if os.path.exists('fort.13'):
        os.remove('fort.13')        
    if os.path.exists('fort.20'):
        os.remove('fort.20')    
    if os.path.exists('fort.35'):
        os.remove('fort.35')    
    if os.path.exists('fort.71'):
        os.remove('fort.71')    
    if os.path.exists('fort.9'):
        os.remove('fort.9')    
    if os.path.exists('fort.91'):
        os.remove('fort.91')    
    if os.path.exists('fort.98'):
        os.remove('fort.98')    
    if os.path.exists('output.pdb'):
        os.remove('output.pdb')
    if os.path.exists('moldyn.vel'):
        os.remove('moldyn.vel')
    if os.path.exists('output.MOP'):
        os.remove('output.MOP')
    if os.path.exists('molfra.out'):
        os.remove('molfra.out')
    if os.path.exists('trainset.in'):
        os.remove('trainset.in')
    if os.path.exists('fort.25'):
        os.remove('fort.25')
    if os.path.exists('fort.3'):
        os.remove('fort.3')
    if os.path.exists('fort.4'):
        os.remove('fort.4')
    if os.path.exists('fort.45'):
        os.remove('fort.45')
    if os.path.exists('fort.62'):
        os.remove('fort.62')            
    if os.path.exists('fort.7'):
        os.remove('fort.7')            
    if os.path.exists('fort.72'):
        os.remove('fort.72')            
    if os.path.exists('fort.73'):
        os.remove('fort.73')            
    if os.path.exists('fort.79'):
        os.remove('fort.79')
    if os.path.exists('fort.83'):
        os.remove('fort.83')
    if os.path.exists('fort.90'):
        os.remove('fort.90')
    if os.path.exists('fort.21'):
        os.remove('fort.21')                                                            

    
    
