from track import *
import numpy as np
from lmfit import models

lengte = '30cm'
voorwerp = 'pil'

folder = 'data/'
file = 'fit_results_'+voorwerp+'_'+lengte+'.txt'


d = open(folder + file)
start = d.readline() # remove first non date line

x = d.readline()
raw_data = []
while x:
    x = x.replace('\n', '')
    x = x.split(',')
    raw_data.append([float(x[0]), float(x[1]), float(x[3])])
    x = d.readline()
d.close() # close the data file


pil_size = []
pil_a = []
pil_a_err = []

for i in raw_data:
    pil_size.append(i[2])
    pil_a.append(i[0])
    pil_a_err.append(i[1])

plt.errorbar(pil_size, pil_a, yerr=pil_a_err, ecolor='black', capsize=1, fmt='none')
plt.ylabel("a voor y=ax")
plt.xlabel("Lengte van de "+voorwerp)
plt.show()