import math as m

def get_translated_position(d): # Translate the x and y coordinates of the ball into a single direction, give as input the openend file
    x = d.readline()
    positions = []
    while x:
        data = x.split(",")
        # turn the strings into floats
        data[1] = float(data[1])
        data[2] = float(data[2])
        data[3] = float(data[3])
        # get the distance using Pythagoras
        distance = m.sqrt(m.pow(data[2], 2) + m.pow(data[3], 2))
        positions.append([data[1], distance])
        x = d.readline()
    return positions

def get_pixels_per_second(pos): # geef de getransleerde positie in enkele richting mee aan de functie
    velocities = []
    for i in range(len(pos) - 1):
        delta_x = pos[i][1] + pos[i+1][1]
        delta_t = pos[i][0] + pos[i+1][0]
        velocity = delta_x/delta_t
        velocities.append([[pos[i][0], pos[i+1][0]], velocity])
    return velocities

# get start values
folder = "Meeting 1"
data = open("data/" + folder + "/data.ascii")
start = data.readline() # remove first non date line

length_file = open("data/" + folder + "/lengte.ascii")
start = length_file.readline() # remove first non date line

# get the length and close the file
length = length_file.readline()
length_file.close()

pos = get_translated_position(data)
velocities = get_pixels_per_second(pos)

data.close()
