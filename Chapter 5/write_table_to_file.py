import numpy as np
import matplotlib.pyplot as plt
import os


def write_table_to_file(f, xmin, xmax, nx, ymin, ymax, ny,
width=10, decimals=0,
filename='table.txt'):
    x1 = np.linspace(xmin, xmax, nx)    # Initiate np arrays
    y1 = np.linspace(ymin, ymax, ny)
    result = np.zeros((len(x1),len(y1)))
    format = ("%" + str(width) +  "." + str(decimals) + "g")    # Format for printing the numbers

    for count_x,x in enumerate(x1):     # Change to for count_x in range(len(x1))
        for count_y,y in enumerate(y1):
            result[count_x,count_y] = eval(f)   # Calculate f(x,y)


    folder_path = "C:\CongLuan\Courses\Python basics\Exercises\Python-basic\Chapter 5"
    abs_path = os.path.join(folder_path, filename)
    with open(abs_path, 'w') as outfile:    # Write to file abs_path
        for row in range(len(x1)+1):
            if row == len(x1):      # If the final row is reached
                outfile.write("          ")     # Create a small space for final row
                for col in range(len(y1)): outfile.write(format %y1[col])   # Write y values for final row
                
            else:
                outfile.write(format %x1[row])
                for col in range(len(y1)): 
                    # print(result[row][col])
                    outfile.write(format  %result[row][col])    # Write values from f(x,y)
            outfile.write("\n")
 
       
    


# res = write_table_to_file(f = "5*x + 2*y", xmin=0, xmax=5, nx=10, ymin=0, ymax=5, ny=10)
# print(res)
write_table_to_file(f = "5*x + 2*y", xmin=0, xmax=8, nx=10, ymin=0, ymax=8, ny=10, width = 10, decimals=4)