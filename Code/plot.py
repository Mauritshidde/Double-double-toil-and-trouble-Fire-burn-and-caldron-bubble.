from track import *
import numpy as np
from lmfit import models

# set the folder to the folder of a measurement.
folder = '18jun/07_pil3_34cm'

# def distance_time_plot(distance, cmp):


# # get start values
length = get_length(folder)
data = get_data_from_file(folder)
cmp = get_cm_per_pixel(data, length)
dist, time = get_dist_traveled(data)
time = np.array(time)  # Convert time to a NumPy array once
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

## zonder c
def fit_func_no_c(x, a, b):
    d = a * x**b
    return d
##

dist_sqr_cm = []
for i in dist_cm:
    dist_sqr_cm.append(i**2)

mod_dist = models.Model(fit_func)
fit = mod_dist.fit(dist_cm, x=time, a=3, b=2, c=0)

## zonder c
mod_dist_no_c = models.Model(fit_func_no_c)
fit_no_c = mod_dist_no_c.fit(dist_cm, x=time, a=3, b=0.5)
##

# fit plot 
d = plt.plot(time, fit.best_fit, label=['y = ax^b + c', 'a='+str(float(fit.params["a"])), 'b='+str(float(fit.params["b"])), 'c='+str(float(fit.params["c"]))])
plt.scatter(time, dist_cm, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(fit.fit_report())

# fit plot zonder c
d_no_c = plt.plot(time, fit_no_c.best_fit, label=['y = ax^b', 'a='+str(float(fit_no_c.params["a"])), 'b='+str(float(fit_no_c.params["b"]))])
plt.scatter(time, dist_cm, s=1)
plt.legend(handles=d_no_c, loc='upper right')
plt.show()
print(fit_no_c.fit_report())

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
d = plt.plot(time, lin_fit.best_fit, label=['y = ax + b', 'a='+str(float(fit.params["a"])), 'b='+str(float(fit.params["b"]))])
plt.scatter(time, dist_sqr_cm, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(lin_fit.fit_report())

## ========== NIEUW ========== ##

# plot data to log log scale
plt.scatter(time - 1.1, np.array(dist_cm), s=1)
plt.xscale('log')
plt.yscale('log')
plt.xlabel("tijd in seconden (log(s))")
plt.ylabel("afstand in cm (log(cm))")
plt.title("Log-Log Scatterplot")
plt.show()

# fit function for log-log scale
def log_log_fit_func(x, a, b):
    d = a * x**b
    return d

# fit model for log-log scale
log_mod = models.Model(log_log_fit_func)
log_fit = log_mod.fit(dist_cm, x=time, a=0.5, b=1.0)

# Plot the fit and data in log-log scale
d = plt.plot(time, log_fit.best_fit, label=['y = ax^b', 'a='+str(float(log_fit.params["a"])), 'b='+str(float(log_fit.params["b"]))], color='red')
plt.scatter(time - 1.1, np.array(dist_cm), s=1)
plt.legend(handles=d, loc='upper right')
import matplotlib.pyplot as plt
plt.xscale('log')
plt.yscale('log')
plt.xlabel("tijd in seconden (log(s))")
plt.ylabel("afstand in cm (log(cm))")
plt.title("Log-Log Fit all Data")
plt.show()
print(log_fit.fit_report())

# log-log fit plot
# Select data in the x-interval from 1 to 100
mask = (time >= 1) & (time <= 100)
time_fit = time[mask]
dist_cm_fit = np.array(dist_cm)[mask]

# Fit only to the selected interval
log_fit = log_mod.fit(dist_cm_fit, x=time_fit, a=0.5, b=1.0)

# Plot fit and data in the selected interval
d_log = plt.plot(time_fit, log_fit.best_fit, label=['y = ax^b', 'a='+str(float(log_fit.params["a"])), 'b='+str(float(log_fit.params["b"]))], color='red')
plt.scatter(time - 1.1, np.array(dist_cm), s=1)
plt.legend(handles=d_log, loc='upper right')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("tijd in seconden (log(s))")
plt.ylabel("afstand in cm (log(cm))")
plt.title("Log-Log Fit in Selected Interval")
plt.show()
print(log_fit.fit_report())

# gebruik de laatste fit om de waarde van a en b te bepalen in normale plot
a = float(log_fit.params["a"])
b = float(log_fit.params["b"])
# Plot the data with the fitted line
plt.scatter(time, dist_cm, s=1)
plt.plot(time, a * time**b, color='red', label=f'Fit: y = {a:.2f} * x^{b:.2f}')
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in cm")
plt.title("lijn gefit via logspace op 1<x<100")
plt.legend()
plt.show()

# log-log fit plot
# Select data in the x-interval from 100 to 1000
mask = (time >= 100) & (time <= 1000)
time_fit = time[mask]
dist_cm_fit = np.array(dist_cm)[mask]

# Fit only to the selected interval
log_fit = log_mod.fit(dist_cm_fit, x=time_fit, a=0.5, b=1.0)

# Plot fit and data in the selected interval
d_log = plt.plot(time_fit, log_fit.best_fit, label=['y = ax^b', 'a='+str(float(log_fit.params["a"])), 'b='+str(float(log_fit.params["b"]))], color='red')
plt.scatter(time - 1.1, np.array(dist_cm), s=1)
plt.legend(handles=d_log, loc='upper right')
plt.xscale('log')
plt.yscale('log')
plt.xlabel("tijd in seconden (log(s))")
plt.ylabel("afstand in cm (log(cm))")
plt.title("Log-Log Fit in Selected Interval")
plt.show()
print(log_fit.fit_report())

# gebruik de laatste fit om de waarde van a en b te bepalen in normale plot
a = float(log_fit.params["a"])
b = float(log_fit.params["b"])
# Plot the data with the fitted line
plt.scatter(time, dist_cm, s=1)
plt.plot(time, a * time**b, color='red', label=f'Fit: y = {a:.2f} * x^{b:.2f}')
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in cm")
plt.title("lijn gefit via logspace op 100<x<1000")
plt.legend()
plt.show()