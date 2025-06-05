from track import *
# set the folder to the folder of a measurement.
folder = 'Meting 1'

# get start values
length = get_length(folder)
data = get_data_from_file(folder)
vel = get_pixels_per_second(data)
pm = get_cm_per_pixel(data)

time = []
speed = []

for i in range(len(vel)):
    time.append((vel[i][0][1] + vel[i][0][0])/2)
    speed.append(vel[i][1])

for i in range(4):
    print(speed[i])

plt.plot(time, speed)
plt.show()
print(data)
x=[]
y=[]
for i in  range(len(data)):
    x.append(data[i][1])
    y.append(data[i][2])

plt.plot(x, y)
plt.show()
