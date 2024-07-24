abs_path = 'C:\\CongLuan\\Courses\\Python basics\\Exercises\\Python-basic\\Chapter 6\\densities.dat'

with open(abs_path, 'r') as infile:
    lines = infile.readlines()
    dict = {}
    for lines in lines:
        keywords = ''
        for x in lines.split()[:-1]:
            keywords += ('%s' %x + ' ')
        dict[keywords.strip()] = lines.split()[-1]
    print(dict)