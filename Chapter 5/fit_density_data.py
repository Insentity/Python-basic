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
        temperature[count] = data.split("     ")[0] # Obtain the temperature value from the list
        density[count] = data.split("     ")[1]
    return(temperature, density)


def fit(x,y,deg):
    coeff = []
    p = []
    y_pol = []
    plt.figure()
    plt.plot(x, y,'o', label="Data")

    for i in range(len(deg)):
        coeff.append(np.polyfit(x,y,deg[i]))
        p.append(np.poly1d(coeff[i]))
        y_pol.append(p[i](x))
        plt.plot(x,y_pol[i], label="Degree %s" %deg[i])

    
    plt.xlabel("Temperature (C)")
    plt.ylabel("Density (kg/m3)")
    plt.title("Air Density vs Temperature")
    plt.legend()

    

air = read_dat_file("Chapter 5\density_air.dat", 9)
water = read_dat_file("Chapter 5\density_water.dat", 8)
# print(len(air))
air_temperature, air_density = filter(air)
water_temperature, water_density = filter(water)

fit(air_temperature, air_density, [1,2])
fit(water_temperature, water_density, [1,2,3])
# fit(air_temperature, air_density, [5])
plt.show()
