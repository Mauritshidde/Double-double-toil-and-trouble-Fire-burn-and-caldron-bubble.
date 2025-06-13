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

mod_dist = models.Model(fit_func)
fit = mod_dist.fit(dist_cm, x=time, a=3, b=2, c=0, weights=np.sqrt(1/np.array([0.5] * len(data))))
plt.plot(time, fit.best_fit)
plt.scatter(time, dist_cm, s=1)
plt.show()
print(fit.fit_report())

f = fit_func(time, fit.params["a"], fit.params["b"], fit.params["c"])
print(len(f))
print(len(dist_cm))

# The residual
plt.plot(dist_cm-f)
plt.show()