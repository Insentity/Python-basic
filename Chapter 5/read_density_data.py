import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_dat_file(path):
    df = pd.read_csv(path)
    df = df.iloc[2:11].iloc[:,0:1]
    df = df.iloc[:,0].tolist()
    # print(df)
    # df = df.tolist()
    return(df)


def filter(nparray):
    # print(nparray[4])
    temperature = np.zeros(len(nparray))
    density = np.zeros(len(nparray))
    for count,data in enumerate(nparray):
        # print(type(data))
        temperature[count] = data.split("     ")[0]
        density[count] = data.split("     ")[1]
    return(temperature, density)


def plot_density(x,y):
    plt.plot(x, y)
    plt.xlabel("Temperature (C)")
    plt.ylabel("Density (kg/m3)")
    plt.show()



air = read_dat_file("Chapter 5\density_air.dat")
# water = read_dat_file("Chapter 5\density_water.dat")
# print(len(air))
air_temperature, air_density = filter(air)
# water_temperature, water_density = filter(water)
plot_density(air_temperature, air_density)
