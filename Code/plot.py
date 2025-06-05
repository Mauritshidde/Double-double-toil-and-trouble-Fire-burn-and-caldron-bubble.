from track import *
import numpy as np
from lmfit import models
# set the folder to the folder of a measurement.
folder = 'Meting 1'

# get start values
length = get_length(folder)
data = get_data_from_file(folder)
vel = get_pixels_per_second(data)
cmp = get_cm_per_pixel(data, length)
# vels = noise_supression(vel, 30)
vels = get_pixels_per_second_suppresed(data, 30)
distance = get_distance_per_time_suppresed(data, 5)
# def fit_function (U_cell, I_L, I_0, A):
#     y = a * x + b
#     return y

time = []
speed = []

for i in range(len(vels)):
    time.append((vels[i][0][1] + vels[i][0][0])/2)
    speed.append(vels[i][1])

# plt.plot(time, speed)
# plt.show()

x=[]
y=[]
for i in  range(len(data)):
    x.append(data[i][1])
    y.append(data[i][2])

# plt.plot(x, y)
# plt.show()

# distance plot plot voor de positie over tijd
current_dist = 0
traveled = [0]
time = [0]
for i in distance:
    current_dist += i[1]
    traveled.append(current_dist * cmp)
    time.append(i[0])

# plt.plot(traveled, time)
plt.scatter(time, traveled, s=0.7)
plt.show()
