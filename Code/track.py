import math as m

def get_data_from_file(d): # Data from file
    x = d.readline()
    raw_data = []
    while x:
        data = x.split(",")
        # turn the strings into floats
        data[1] = float(data[1])
        data[2] = float(data[2])
        data[3] = float(data[3])
        # get the distance using Pythagoras
        raw_data.append([data[1], data[2], data[3]])
        x = d.readline()
    d.close() # close the data file
    return raw_data

def get_pixels_per_second(pos): # geef de getransleerde positie in enkele richting mee aan de functie
    velocities = []
    for i in range(len(pos) - 1):
        delta_y = pos[i+1][2] - pos[i][2]
        delta_x = pos[i+1][1] - pos[i][1]
        delta_t = pos[i+1][0] - pos[i][0]
        velocity = m.sqrt(delta_x**2 + delta_y**2)/delta_t
        velocities.append([[pos[i][0], pos[i+1][0]], velocity])
    return velocities

def get_cm_per_pixel(data): # calulate how many cm a pixel is
    delta_x = data[0][1] - data[-1][1]
    delta_y = data[0][2] - data[-1][2]
    tot_dist_pixels = m.sqrt(delta_x**2 + delta_y**2)
    print(length/tot_dist_pixels, length, tot_dist_pixels)
    return tot_dist_pixels


# get start values
folder = "Meting 1"
data = open("data/" + folder + "/data.ascii")
start = data.readline() # remove first non date line

length_file = open("data/" + folder + "/lengte.ascii")
start = length_file.readline() # remove first non date line

# get the length and close the file
length = float(length_file.readline())
length_file.close()

data = get_data_from_file(data)
vel = get_pixels_per_second(data)
pm = get_cm_per_pixel(data)

print(vel[0][1] * pm, " cm per seconde")

for i in vel:
    print(i)
# start calculating




# pos = get_translated_position(data)
# velocities = get_pixels_per_second(pos)

# pos[]
#
# for i in velocities:
#     print(i)
