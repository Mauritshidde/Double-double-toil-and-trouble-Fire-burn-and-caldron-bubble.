from track import *
import numpy as np
from lmfit import models

# set the folder to the folder of a measurement.
folder = 'dag1/Meting 1'

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