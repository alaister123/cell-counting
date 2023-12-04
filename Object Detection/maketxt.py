import pandas as pd
import numpy as np
import os


width = 800
height = 600

xwidth = 10/width
ywidth = 10/height

file = [i for i in os.listdir() if ".csv" in i]



for i in range(len(file)):
    result = pd.DataFrame()
    data = pd.read_csv(file[i])
    #data = data.drop(columns=['Z'])
    result['X'] = data['X']/width
    result['Y'] = data['Y']/height
    result.insert(0, 'class', 0) 
    result['xwidth'] = xwidth
    result['ywidth'] = ywidth
    save_to = file[i].replace('.csv','.txt')
    result.to_csv(save_to, header=None, index=None, sep=' ', mode='a')


