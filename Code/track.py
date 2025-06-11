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

def get_data_from_file(folder):
    data = open("data/" + folder + "/data.mqa")
    start = data.readline() # remove first non date line

    length_file = open("data/" + folder + "/lengte.mqa")
    start = length_file.readline() # remove first non date line

    # get the length and close the file
    length = float(length_file.readline())
    length_file.close()

    return get_data_from_file_helper(data)

def get_length(folder):
    length_file = open("data/" + folder + "/lengte.mqa")
    start = length_file.readline()
    length = float(length_file.readline())
    length_file.close()
    return length


def get_cm_per_pixel(data, length): # calulate how many cm a pixel is
    delta_x = data[0][1] - data[-1][1]
    delta_y = data[0][2] - data[-1][2]
    tot_dist_pixels = m.sqrt(delta_x**2 + delta_y**2)
    return length/tot_dist_pixels

def get_dist_traveled(data):
    dist = 0
    dists = [0]
    time = [0]
    for i in range(len(data) - 1):
        dist += pow(data[i][2] - data[i+1][2], 2)
        dists.append(dist)
        time.append(data[i][2])
    return dists, time

def dist_in_cm(dist, cmp):
    dist2 = dist.copy()
    for i in range(len(dist)):
        dist2[i] = dist[i] * cmp

    return dist2