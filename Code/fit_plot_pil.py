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
    raw_data.append([float(x[0]), float(x[1]), float(x[3]), float(x[4])])
    x = d.readline()
d.close() # close the data file

datas = [[raw_data[0], raw_data[1], raw_data[2],raw_data[3],raw_data[4],raw_data[5]], [raw_data[6], raw_data[7],raw_data[8],raw_data[9],raw_data[10]]]

pil_size = []
pil_a = []
pil_a_err = []

for raw_datas in datas:
    pil_size_h = []
    pil_a_h = []
    pil_a_err_h = []
    for i in raw_datas:
        pil_size_h.append(i[2])
        pil_a_h.append(i[0])
        pil_a_err_h.append(i[1])
    pil_size.append(pil_size_h)
    pil_a.append(pil_a_h)
    pil_a_err.append(pil_a_err_h)

plt.errorbar(pil_size[0], pil_a[0], yerr=pil_a_err[0], ecolor='black', capsize=1, fmt='none', color='red', label='druk = 100')
plt.errorbar(pil_size[1], pil_a[1], yerr=pil_a_err[1], ecolor='orange', capsize=1, fmt='none', color='pink', label='druk = 125')
plt.ylabel("a voor y=ax")
plt.xlabel("Lengte van de "+voorwerp)
plt.legend()
plt.show()