'''
Code for reading the data from data file from the measurements
The functions in this file should be imported into another file and not used in this file
The functions are for translating the movemend in the x and y direction to a general direction up,
because the camera isn't always straight. And calculating the velocity of the object in pixels per second
'''
import math as m
import matplotlib.pyplot as plt

def get_data_from_file_helper(d): # Data from file
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

def get_pixels_per_second_suppresed(pos, steps):
    velocities = []
    i = steps
    for j in range(len(pos) - 1 - 2 * steps):
        delta_y = abs(pos[i-steps][2] - pos[i+steps][2])
        delta_x = abs(pos[i-steps][1] - pos[i+steps][1])
        delta_t = abs(pos[i-steps][0] - pos[i+steps][0])
        velocity = m.sqrt(delta_x**2 + delta_y**2)/delta_t
        velocities.append([[pos[i][0], pos[i+1][0]], velocity])
        i+=1
    return velocities

def get_distance_per_time_suppresed(pos, steps):
    velocities = []
    i = steps
    for j in range(len(pos) - 1 - 2 * steps):
        delta_y = abs(pos[i-steps][2] - pos[i+steps][2])
        delta_x = abs(pos[i-steps][1] - pos[i+steps][1])
        delta_t = pos[i-steps][0] + pos[i+steps][0]
        distance = m.sqrt(delta_x**2 + delta_y**2)
        velocities.append([delta_t/2, distance])
        i+=1
    return velocities

def get_cm_per_pixel(data, length): # calulate how many cm a pixel is
    delta_x = data[0][1] - data[-1][1]
    delta_y = data[0][2] - data[-1][2]
    tot_dist_pixels = m.sqrt(delta_x**2 + delta_y**2)
    return length/tot_dist_pixels

def get_data_from_file(folder):
    data = open("data/" + folder + "/data.ascii")
    start = data.readline() # remove first non date line

    length_file = open("data/" + folder + "/lengte.ascii")
    start = length_file.readline() # remove first non date line

    # get the length and close the file
    length = float(length_file.readline())
    length_file.close()

    return get_data_from_file_helper(data)

def get_length(folder):
    length_file = open("data/" + folder + "/lengte.ascii")
    start = length_file.readline()
    length = float(length_file.readline())
    length_file.close()
    return length

def noise_supression(vel, steps): # depens on a velocity set that is big
    suppresed_vel = []
    i = steps
    for j in range(len(vel) - steps*2):
        vel_tot = vel[i][1]
        for k in range(steps):
            vel_tot += vel[i-k-1][1]
            vel_tot += vel[i+k+1][1]
        suppresed_vel.append([vel[i][0], vel_tot/(steps + 1)])
        i+=1
    return suppresed_vel
