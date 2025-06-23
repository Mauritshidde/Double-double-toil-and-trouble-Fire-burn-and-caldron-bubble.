from track import *
import numpy as np
from lmfit import models

# set the folder to the folder of a measurement.
folder = '20jun/06_pil5_30cm'
folder2 = 'data/20jun/06_pil5_30cm'
# def distance_time_plot(distance, cmp):
file = open(folder2 + "/fit_data.txt", "w")

# # get start values
length = get_length(folder)
data = get_data_from_file(folder)
cmp = get_cm_per_pixel(data, length)
dist, time = get_dist_traveled(data)
time = np.array(time)  # demofileConvert time to a NumPy array once
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
plt.show()

# fit plot 
d = plt.plot(time, fit.best_fit, label=['y = ax^b + c', 'a='+str(float(fit.params["a"])), 'b='+str(float(fit.params["b"])), 'c='+str(float(fit.params["c"]))])
plt.scatter(time, dist_cm, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(fit.fit_report())
# with open(folder2 + "/fit_data.txt", "w") as f:
file.write("\n at plot \n \n")
file.writelines(fit.fit_report())


# fit plot zonder c
d_no_c = plt.plot(time, fit_no_c.best_fit, label=['y = ax^b', 'a='+str(float(fit_no_c.params["a"])), 'b='+str(float(fit_no_c.params["b"]))])
plt.scatter(time, dist_cm, s=1)
plt.legend(handles=d_no_c, loc='upper right')
plt.show()
print(fit_no_c.fit_report())
# with open(folder2 + "/fit_data.txt", "w") as f:
file.write("\n at plot zonder c \n \n")
file.writelines(fit_no_c.fit_report())

f = fit_func(time, fit.params["a"], fit.params["b"], fit.params["c"])
print(len(f))
print(len(dist_cm))


#afstand kwadraat tijd plot
print("ja")
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
file.write("\n lin fit \n \n")
file.writelines(lin_fit.fit_report())

#lin fit van fit
lin_fitmod = models.Model(lin_fit_func)
lin_fitfit = lin_fitmod.fit(fit.best_fit * fit.best_fit, x=time, a=2, b=3)

d = plt.plot(time, lin_fitfit.best_fit, label=['y = ax + b', 'a='+str(float(lin_fitfit.params["a"])), 'b='+str(float(lin_fitfit.params["b"]))])
plt.scatter(time, fit.best_fit * fit.best_fit, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(lin_fitfit.fit_report())
file.write("\n lin fit met at fit \n \n")
file.writelines(lin_fitfit.fit_report())

def lin_fit_func2(x, a):
    d = a * x
    return d

lin_mod = models.Model(lin_fit_func2)
lin_fit = lin_mod.fit(dist_sqr_cm, x=time, a=2, b=3)

d = plt.plot(time, lin_fit.best_fit, label=['y = ax', 'a='+str(float(lin_fit.params["a"]))])
plt.scatter(time, dist_sqr_cm, s=1)
plt.legend(handles=d, loc='upper right')
plt.show()
print(lin_fit.fit_report()) 
file.write("\n lin fit zonder b \n \n")
file.writelines(lin_fit.fit_report())
