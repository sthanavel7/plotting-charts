import pandas as pd;
import numpy as np;

df = pd.read_csv('merged.csv');

SI_mass = [];
SI_radius = [];

for i in df['solar_mass'].tolist():
    val = float(i) * 1.989e+30;
    SI_mass.append(val);
    
for i in df['solar_radius'].tolist():
    val = float(i) * 6.957e+8;
    SI_radius.append(val);
    
gravity = [];

for i in range(0, int(len(SI_mass))):
    gravity_val = float(SI_mass[i] * 6.67e-11)//float(SI_radius[i] ** 2);
    gravity.append(gravity_val);

dict = {'gravity' : gravity};

gravityDF = pd.DataFrame(dict);
gravityDF.to_csv('/Users/mananjain/Desktop/Solar Planets Prtc/gravity.csv');

gravity_merged_data = pd.concat(
    map(pd.read_csv, ['merged.csv', 'gravity.csv']), ignore_index=True, axis=1);

del gravity_merged_data[6]
del gravity_merged_data[1]
del gravity_merged_data[0]

print(gravity_merged_data);

gravity_merged_data.to_csv('/Users/mananjain/Desktop/Solar Planets Prtc/gravity_merged_data.csv');