from track import *
import numpy as np
from lmfit import models

# set the folder to the folder of a measurement.
folder = 'dag1/Meting 4'

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

plt.scatter(time, dist_cm, s=1)
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in cm")
plt.show()

def fit_func(x, a, b, c):
    d = a * x**b + c
    return d

def fit_func2(x, a):
    d = (a * (m.e**x/(1+m.e**x)))**0.5
    return d

dist_sqr_cm = []
for i in dist_cm:
    dist_sqr_cm.append(i**2)

mod_dist2 = models.Model(fit_func2)
fit2 = mod_dist2.fit(dist_cm, x=time, a=3, weights=np.sqrt(1/(np.array(0.5)*len(dist_cm))))

mod_dist = models.Model(fit_func)
fit = mod_dist.fit(dist_cm, x=time, a=3, b=2, c=0)
plt.plot(time, fit.best_fit)
plt.plot(time, fit2.best_fit)
plt.scatter(time, dist_cm, s=1)
plt.show()
print(fit.fit_report())
print(fit2.fit_report())

f = fit_func(time, fit.params["a"], fit.params["b"], fit.params["c"])
print(len(f))
print(len(dist_cm))


#verschil b met wortel
plt.scatter(time, dist_sqr_cm, s=1)
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in cm^2")
plt.show()
print(fit.fit_report())

# The residual
plt.plot(time, dist_cm-f)
plt.show()
errs = dist_cm-f

# plot met wieghts 
plt.plot(time, fit.best_fit)
plt.scatter(time, dist_cm, s=1, y_err=errs)
plt.show()
print(fit.fit_report())