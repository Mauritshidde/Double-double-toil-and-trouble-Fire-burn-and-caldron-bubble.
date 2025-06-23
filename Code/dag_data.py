from track import *
import numpy as np
from lmfit import models

# set the folder to the folder of a measurement.
folders = {
    '17jun': ['01_tetraederbodem_10cm', '02_tetraederpiek_12cm', '04_Cilinder5_8cm'],
    '18jun': ['01_bol_34cm', '02_pil1_34cm', '03_pil1_34cm', '04_pil1_34cm', '05_bol_34cm', '06_pil2_34cm', '07_pil3_34cm', '08_pil2_42cm', '09_pil3_34cm', '10_pil3_42cm', '11_pil4_34cm', '12_pil4_42cm', '13_pil5_32cm'],
    '19jun': ['01_verticale_ellips_34cm', '02_verticale_ellips2_34cm', '03_verticale_ellips2_34cm', '04_pil1_30cm', '05_pil1_30cm', '06_pil2_30cm', '07_pil3_30cm', '08_pil4_30cm', '09_pil5_30cm'],
    '20jun': ['01_bol_30cm', '02_pil1_30cm', '03_pil2_30cm', '04_pil3_30cm', '05_pil4_30cm', '06_pil5_30cm']
}

# # get start values

def get_fit_data(folder):
    length = get_length(folder)
    data = get_data_from_file(folder)
    cmp = get_cm_per_pixel(data, length)
    dist, time = get_dist_traveled(data)
    time = np.array(time)  # demofileConvert time to a NumPy array once
    dist_cm = dist_in_cm(dist, cmp)
    print(data)

files = []
for day in folders:
    day_files = folders.get(day)
    for i in day_files:
        folder = day + "/" + i
        print(folder)
        get_fit_data(folder)

        # files.append(i)
print(files)

# plt.scatter(time, dist, s=1)
# plt.xlabel("tijd in seconden")
# plt.ylabel("afstand in pixels")
# plt.show()

