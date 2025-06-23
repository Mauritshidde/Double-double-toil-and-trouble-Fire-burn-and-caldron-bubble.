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

# fit aan de resultaten
mod = models.Model(lambda x, a, b, c, d: a * x**3 + b * x**2 + c * x + d)
fit1 = mod.fit(pil_a[0], x=pil_size[0], a=0, b=1, c=0, d=0)
fit2 = mod.fit(pil_a[1], x=pil_size[1], a=0, b=1, c=0, d=0)

plt.errorbar(pil_size[0], pil_a[0], yerr=pil_a_err[0], ecolor='black', capsize=1, fmt='none', color='red', label='druk = 100')
plt.errorbar(pil_size[1], pil_a[1], yerr=pil_a_err[1], ecolor='orange', capsize=1, fmt='none', color='pink', label='druk = 125')

a1, b1, c1, d1 = fit1.best_values['a'], fit1.best_values['b'], fit1.best_values['c'], fit1.best_values['d']
a2, b2, c2, d2 = fit2.best_values['a'], fit2.best_values['b'], fit2.best_values['c'], fit2.best_values['d']
print(f"Fit 1 parameters: a={a1}, b={b1}, c={c1}, d={d1}")
print(f"Fit 2 parameters: a={a2}, b={b2}, c={c2}, d={d2}")
x_fit = np.arange(2, 6.1, 0.1)
y_fit1 = a1 * x_fit**3 + b1 * x_fit**2 + c1 * x_fit + d1
y_fit2 = a2 * x_fit**3 + b2 * x_fit**2 + c2 * x_fit + d2
plt.plot(x_fit, y_fit1, color='red', label=f'fit 100 druk: {round(a1, 2)}x^3+{round(b1, 2)}x^2+{round(c1, 2)}x+{round(d1, 2)}')
plt.plot(x_fit, y_fit2, color='pink', label=f'fit 125 druk: {round(a2, 2)}x^3+{round(b2, 2)}x^2+{round(c2, 2)}x+{round(d2, 2)}')

plt.scatter(pil_size[0], pil_a[0], color='magenta')
plt.scatter(pil_size[1], pil_a[1], color='cyan')

plt.ylabel("a voor y=ax")
plt.xlabel("Lengte van de "+voorwerp)
plt.legend()
plt.show()