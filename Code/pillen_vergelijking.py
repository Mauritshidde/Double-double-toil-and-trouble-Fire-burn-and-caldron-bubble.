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

# 19 juni data
meting_nums_19 = range(4, 10)
pil_nums_19 = [1, 1, 2, 3, 4, 5]
afstanden_19 = [30, 30, 30, 30, 30, 30]
a_vals_19, b_vals_19 = [], []

for idx, meting in enumerate(meting_nums_19):
    pil_num = pil_nums_19[idx]
    afstand = afstanden_19[idx]
    folder = f'19jun/{str(meting).zfill(2)}_pil{pil_num}_{afstand}cm' if pil_num != -1 else f'19jun/01_bol_{afstand}cm'
    length = get_length(folder)
    data = get_data_from_file(folder)
    cmp = get_cm_per_pixel(data, length)
    dist, time = get_dist_traveled(data)
    dist_cm = dist_in_cm(dist, cmp)
    time = np.array(time)
    mask = (time >= 1) & (time <= 100)
    time_fit = time[mask]
    dist_cm_fit = np.array(dist_cm)[mask]
    mod = models.Model(lambda x, a, b: a * x**0.5)
    fit = mod.fit(dist_cm_fit, x=time_fit, a=0.5, b=1.0)
    a_vals_19.append(float(fit.params['a']))
    b_vals_19.append(float(fit.params['b']))

plt.plot(np.array(pil_nums_19)+1, a_vals_19, 'ro', label='19 juni')
plt.plot(np.array(pil_nums)+1, a_vals, 'o', label='18 juni')
plt.xlabel('lengte horizontale wand pil (cm)')
plt.ylabel('a uit fit y = a*x^0.5')
plt.title('a per pil')
plt.legend()
plt.show()

model = models.Model(lambda x, a, b, c: a * x**b + c)
# Combine the actual lengths and a-values for both days
# Take only the first and last data point of 18 juni
a_vals_selected = [a_vals[0], a_vals[-1]]
pil_nums_selected = [pil_nums[0], pil_nums[-1]]

# Exclude the last data point of 19 juni
a_vals_19_selected = a_vals_19[:-1]
pil_nums_19_selected = pil_nums_19[:-1]

sort_idx = np.argsort(np.array(a_vals_selected + a_vals_19_selected))

# Combine for fitting
all_a_vals = np.array(a_vals_selected + a_vals_19_selected)[sort_idx]
alle_pil_muurhoogtes = np.array(pil_nums_selected + pil_nums_19_selected)[sort_idx] + 2

# fit
fit = model.fit(all_a_vals, x=alle_pil_muurhoogtes, a=1, b=1, c=1)
plt.plot(np.array(alle_pil_muurhoogtes)-1, all_a_vals, 'o', label='Data')
plt.xlabel('lengte horizontale wand pil (cm)')
plt.ylabel("Zinksnelheid (coëfficiënt uit de wortel fit)")
a = fit.params['a'].value
b = fit.params['b'].value
c = fit.params['c'].value
x_fit = np.arange(1, 7.01, 0.01)
plt.plot(x_fit-1, fit.eval(x=x_fit), 'r-', label=f'y= {a:.{4}g}*x^{b:.{4}g} + {c:.{4}g}')
plt.legend()
plt.show()
print(f'Fitted parameters: a={a:.{4}g}, b={b:.{4}g}, c={c:.{4}g}')
# plt.plot(np.array(pil_nums)+1, b_vals, 'o')
# plt.xlabel('lengte horizontale wand pil (cm)')
# plt.ylabel('b uit fit y = a*x^b')
# plt.title('b per pil')
# plt.show()