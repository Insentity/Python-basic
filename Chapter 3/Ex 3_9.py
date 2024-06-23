import numpy as np

def sum(x):
    """
    This function calculates the sum of the arguments. 
    The argument can be a 1D list, 2D list or list of string

    x: Input argument
    return: sum "result"

    """
    global total
    def sum_1():
        global total
        for i in x:
            # print(i)
            total += i
        return total
    
    
    if len(np.shape(x)) == 2: 
        # print(1)
        # print(len(np.shape(x)))
        total = []
        result = sum_1()
    elif isinstance(x[0],str):
        # print(2)
        total = []
        result = ''.join(sum_1())
    else: 
        # print(3)
        total = 0
        result = sum_1()

    return(result)

# result = sum([[1,2],[1,2],[1,4]])
# result = sum([1,2,4,5])
result = sum(["hello" ," ", "world"])
print(result)





    