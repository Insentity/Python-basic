import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def read_dat_file(path,length):     # Path is the path to the .dat file, length is the number of rows that contain the density values
    df = pd.read_csv(path)      # Convert to pandas dataframe
    df = df.iloc[2:length+2].iloc[:,0:1]
    # iloc[2:length+2] slice df from row 2 to row length+2, starts from 2 to remove the headings. length+2 since we starts at index 2
    # iloc[:,0:1] slide the resulting df to only column 0
    df = df.iloc[:,0].tolist()  # Convert dataframe to python list
    return(df)


def filter(nparray):
    # print(nparray[4])
    temperature = np.zeros(len(nparray))    # Initialize np array
    density = np.zeros(len(nparray))
    for count,data in enumerate(nparray):
        print(data.split("     ")[0])   # Split the temperature values from density
        temperature[count] = data.split("     ")[0] # Obtain the temperature value from the list
        density[count] = data.split("     ")[1]
    return(temperature, density)


def plot_density(x,y, title):
    plt.figure()
    plt.plot(x, y)
    plt.xlabel("Temperature (C)")
    plt.ylabel("Density (kg/m3)")
    plt.title(title)
    



air = read_dat_file("Chapter 5\density_air.dat", 9)
water = read_dat_file("Chapter 5\density_water.dat", 8)
# print(len(air))
air_temperature, air_density = filter(air)
water_temperature, water_density = filter(water)
plot_density(air_temperature, air_density, "Air density vs Temperature")
plot_density(water_temperature, water_density, "Water density vs Temperature")
plt.show()

