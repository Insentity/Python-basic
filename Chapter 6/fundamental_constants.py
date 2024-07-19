import numpy as np

abs_path = "C:\\CongLuan\\Courses\\Python basics\\Exercises\\Python-basic\\Chapter 6\\constants.txt"

with open(abs_path, "r") as infile:
    lines = infile.readlines()
    lines = lines[2:]
    dict = {}
    for lines in lines:
        print(lines.split()[:-2])
        dict[lines.split()[:-2]] = 1
    # print(lines)


