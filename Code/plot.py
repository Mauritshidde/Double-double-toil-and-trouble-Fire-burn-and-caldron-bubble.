from track import *
import numpy as np
from lmfit import models

# set the folder to the folder of a measurement.
folder = '18jun/13_pil5_32cm'

# def distance_time_plot(distance, cmp):


# # get start values
length = get_length(folder)
data = get_data_from_file(folder)
cmp = get_cm_per_pixel(data, length)
dist, time = get_dist_traveled(data)
dist_cm = dist_in_cm(dist, cmp)

plt.scatter(time, dist, s=1)
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in pixels")
plt.show()

# dt graph
plt.scatter(time, dist_cm, s=1)
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in cm")
plt.show()

def fit_func(x, a, b, c):
    d = a * x**b + c
    return d

dist_sqr_cm = []
for i in dist_cm:
    dist_sqr_cm.append(i**2)

mod_dist = models.Model(fit_func)
fit = mod_dist.fit(dist_cm, x=time, a=3, b=2, c=0)

# fit plot 
d = plt.plot(time, fit.best_fit, label=['y = ax^b + c', 'a='+str(float(fit.params["a"])), 'b='+str(float(fit.params["b"])), 'c='+str(float(fit.params["c"]))])
plt.scatter(time, dist_cm, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(fit.fit_report())

f = fit_func(time, fit.params["a"], fit.params["b"], fit.params["c"])
print(len(f))
print(len(dist_cm))


#verschil b met wortel
plt.scatter(time, dist_sqr_cm, s=1)
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in cm^2")
plt.show()
print(fit.fit_report())

# The residual van de fit
plt.plot(time, dist_cm-f)
plt.show()
y_err = abs(dist_cm-f)

# scatter met error op basis van fit
plt.scatter(time, fit.best_fit)
plt.scatter(time, dist_cm, color='black')
plt.errorbar(time, dist_cm, yerr=y_err, fmt='none', ecolor='pink', capsize=2)
plt.show()
print(fit.fit_report())

# lineair fit
def lin_fit_func(x, a, b):
    d = a * x + b
    return d

lin_mod = models.Model(lin_fit_func)
lin_fit = lin_mod.fit(dist_sqr_cm, x=time, a=2, b=3)

#lin fit plot
d = plt.plot(time, lin_fit.best_fit, label=['y = ax + b', 'a='+str(float(lin_fit.params["a"])), 'b='+str(float(lin_fit.params["b"]))])
plt.scatter(time, dist_sqr_cm, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(lin_fit.fit_report())

#lin fit van fit
lin_fitmod = models.Model(lin_fit_func)
lin_fitfit = lin_fitmod.fit(fit.best_fit * fit.best_fit, x=time, a=2, b=3)

d = plt.plot(time, lin_fitfit.best_fit, label=['y = ax + b', 'a='+str(float(lin_fitfit.params["a"])), 'b='+str(float(lin_fitfit.params["b"]))])
plt.scatter(time, fit.best_fit * fit.best_fit, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(lin_fitfit.fit_report())