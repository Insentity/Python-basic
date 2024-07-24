import numpy as np

abs_path = "C:\\CongLuan\\Courses\\Python basics\\Exercises\\Python-basic\\Chapter 6\\constants.txt"

with open(abs_path, "r") as infile:
    lines = infile.readlines()
    lines = lines[2:]
    dict = {}
    for lines in lines:
        keywords = '' 
        for x in lines.split()[:-2]:
            keywords += ('%s ' %x)      # Keywords are the constant names. Meaning items before the second last 2
        dict[keywords.strip()] = lines.split()[-2]  # The values of the constants are the second last items obtained from .split()
        # [keywords.strip()] removes any whitespace before and after the strings in "keywords"
    print(dict)


