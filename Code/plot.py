from track import *
import numpy as np
from lmfit import models

# set the folder to the folder of a measurement.
folder = 'Meting 2'

# def distance_time_plot(distance, cmp):


# get start values
length = get_length(folder)
data = get_data_from_file(folder)
vel = get_pixels_per_second(data)
cmp = get_cm_per_pixel(data, length)
print(data[0], data[1], data[2], data[-1], data[-2], data[-3])
print(cmp)
# vels = noise_supression(vel, 30)
vels = get_pixels_per_second_suppresed(data, 30)
distance = get_distance_per_time(data) # suppresed versie werkt niet

# variabelen voor tijd afstand plots
current_dist = 0
traveled = [0]
time = [0]
for i in distance:
    current_dist += i[1]
    traveled.append(current_dist * cmp)
    time.append(i[0])
#afstand tijd plot
plt.scatter(time, traveled, s=0.7)
plt.xlabel("tijd in seconden")
plt.ylabel("afstand in cm")
plt.show()

traveled_arr = np.array(traveled)
plt.scatter(time, traveled_arr**2, s=0.7)
plt.xlabel("tijd in seconden")
plt.ylabel("gekwadrateerde afstand in cm")
plt.show()
