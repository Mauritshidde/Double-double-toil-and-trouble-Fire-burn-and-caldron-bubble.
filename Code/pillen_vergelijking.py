import numpy as np
import matplotlib.pyplot as plt
from track import *
from lmfit import models

# meting_nums = list(range(1, 5)) + list(range(6, 14))
meting_nums = [1, 4, 6, 7, 9, 11, 13]
a_vals, b_vals = [], []

# Define pil_nums and afstanden to match meting_nums
# pil_nums = [-1, 1, 1, 1, 2, 3, 2, 3, 3, 4, 4, 5] # bol is pil nummer -1 :P
# afstanden = [34, 34, 34, 34, 34, 34, 42, 34, 42, 34, 42, 32]

# alleen de kleine vaas
pil_nums = [-1, 1, 2, 3, 3, 4, 5]  # bol is pil nummer -1 :P
afstanden = [34, 34, 34, 34, 34, 34, 32]

def construct_folder_path(meting, pil_num, afstand):
    if pil_num == -1:  # Bol
        return f'18jun/01_bol_{afstand}cm'
    else:
        return f'18jun/{str(meting).zfill(2)}_pil{pil_num}_{afstand}cm'

for idx, meting in enumerate(meting_nums):
    pil_num = pil_nums[idx]
    afstand = afstanden[idx]
    folder = construct_folder_path(meting, pil_num, afstand)
    length = get_length(folder)
    data = get_data_from_file(folder)
    cmp = get_cm_per_pixel(data, length)
    dist, time = get_dist_traveled(data)
    dist_cm = dist_in_cm(dist, cmp)
    time = np.array(time)

    # Fit y = a * x^b in log-log space for 1 < x < 100
    mask = (time >= 1) & (time <= 100)
    time_fit = time[mask]
    dist_cm_fit = np.array(dist_cm)[mask]
    mod = models.Model(lambda x, a, b: a * x**0.5)
    fit = mod.fit(dist_cm_fit, x=time_fit, a=0.5, b=1.0)
    a_vals.append(float(fit.params['a']))
    b_vals.append(float(fit.params['b']))

plt.plot(np.array(pil_nums)+1, a_vals, 'o')
plt.xlabel('lengte horizontale wand pil (cm)')
plt.ylabel('a uit fit y = a*x^b')
plt.title('a per pil')
plt.show()

# plt.plot(np.array(pil_nums)+1, b_vals, 'o')
# plt.xlabel('lengte horizontale wand pil (cm)')
# plt.ylabel('b uit fit y = a*x^b')
# plt.title('b per pil')
# plt.show()