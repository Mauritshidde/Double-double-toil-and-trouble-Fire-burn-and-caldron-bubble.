from track import *
import numpy as np
from lmfit import models
import json

# set the folder to the folder of a measurement.
folders = {
    '17jun': ['01_tetraederbodem_10cm', '02_tetraederpiek_12cm', '04_Cilinder5_8cm'],
    '18jun': ['01_bol_34cm', '02_pil1_34cm', '03_pil1_34cm', '04_pil1_34cm', '05_bol_34cm', '06_pil2_34cm', '07_pil3_34cm', '08_pil2_42cm', '09_pil3_34cm', '10_pil3_42cm', '11_pil4_34cm', '12_pil4_42cm', '13_pil5_32cm'],
    '19jun': ['01_verticaleellips_34cm', '02_verticaleellips2_34cm', '03_verticaleellips2_34cm', '04_pil1_30cm', '05_pil1_30cm', '06_pil2_30cm', '07_pil3_30cm', '08_pil4_30cm', '09_pil5_30cm'],
    # '20jun': ['01_bol_30cm', '02_pil1_30cm', '03_pil2_30cm', '04_pil3_30cm', '05_pil4_30cm', '06_pil5_30cm']
}

# # get start values
def get_fit_data(folder):
    fit_data = {
        'fit1': [],
        'fit2': [],
        'object': [],
        'length': []
    }

    length = get_length(folder)
    data = get_data_from_file(folder)
    cmp = get_cm_per_pixel(data, length)
    dist, time = get_dist_traveled(data)
    time = np.array(time)
    dist_cm = dist_in_cm(dist, cmp)

    def sqrt_fit(x, a, b):
        return a * x**b

    def lin_fit(x, a):
        return a * x

    sqrt_mod = models.Model(sqrt_fit)
    sqrt_fit = sqrt_mod.fit(dist_cm, x=time, a=1, b=0.5)
    sqrt_mod_fit = models.Model(lin_fit)
    lin_fit_fit = sqrt_mod_fit.fit(sqrt_fit.best_fit**2, x=time, a=1)

    dist_sqr = []
    for i in dist_cm:
        dist_sqr.append(i**2)

    lin_mod = models.Model(lin_fit)
    lin_fit = lin_mod.fit(dist_sqr, x=time, a=1)

    # safe fit data
    fit_data['fit1'] = [float(sqrt_fit.params["a"]), float(sqrt_fit.params["b"]), float(lin_fit_fit.params["a"])]
    fit_data['fit2'] = float(lin_fit.params["a"])

    return fit_data

# def to_json(data):
    
#     for i in data:
        
def remove_cm(number):
    result = ''
    print(number)
    for i in number:
        print(i)
        try:
            int(i) # check if i is an number or char
            result += i
        except:
            return int(result)
    return int(result)

def create_json_data():
    metingen = []
    for day in folders:
        day_files = folders.get(day)
        for i in day_files:
            folder = day + "/" + i
            object = i.split("_")[1]
            length = i.split("_")[2]
            length = remove_cm(length)
            print(object, length, folder)
            data = get_fit_data(folder)

            # set size and object
            data['object'] = object
            # data['object_length'] = object
            data['length'] = float(length)
            
            metingen.append(data)

    with open("data/alles.json", "w") as outfile:
        json.dump(metingen, outfile)


def pil_data():
    with open('data/alles.json', 'r') as openfile:
        data = json.load(openfile)

    pil_data = []

    for i in data:
        ob = i.get("object")[0] + i.get("object")[1] + i.get("object")[2]
        print(ob)
        length = 0
        if (ob == "pil" or i.get("object") == "bol"):
            if i.get("object") == "bol":
                length = 0
            else:
                length = i.get("object")[3]

            i['object_length'] = length
            size = i.get("length")
            if (size < 40 and size >=30):
                pil_data.append(i)

    with open("data/pillen.json", "w") as outfile:
        json.dump(pil_data, outfile)

def plot_lin_fit():
    with open('data/pillen.json', 'r') as openfile:
        data = json.load(openfile)

    vals = []
    pill_size = []
    for i in data:
        vals.append(i.get('fit2'))
        pill_size.append(i.get('object_length'))

    plt.scatter(pill_size, vals)
    plt.xlabel("lengte van pil")
    plt.ylabel("zinksnelheid van de indringer")
    plt.show()

option = int(input("Press 1 to create a json file with all the fit results, press 2 to filter out all the non pill data, 3 for lin fit van pillen, press 4 to do all: "))
if option == 1:
    create_json_data()
elif option == 2:
    pil_data()
elif option == 3:
    plot_lin_fit()
else:
    create_json_data()
    pil_data()
    plot_lin_fit()