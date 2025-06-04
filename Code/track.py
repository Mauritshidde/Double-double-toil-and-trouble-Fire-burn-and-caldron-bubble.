import math as m

f = open("data/test.ascii")
start = f.readline()

def get_translated_position(f): # Translate the x and y coordinates of the ball into a single direction, give as input the openend file
    x = f.readline() # read the first line to descard it because it doesn't contain usefull data
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
        x = f.readline()
    return positions

def get_pixels_per_second(pos): # geef de getransleerde positie in enkele richting mee aan de functie
    velocities = []
    for i in range(len(pos) - 1):
        delta_x = pos[i][1] + pos[i+1][1]
        delta_t = pos[i][0] + pos[i+1][0]
        velocity = delta_x/delta_t
        velocities.append([[pos[i][0], pos[i+1][0]], velocity])
    return velocities

pos = get_translated_position(f)
velocities = get_pixels_per_second(pos)

for i in velocities:
    print(i)
f.close()
