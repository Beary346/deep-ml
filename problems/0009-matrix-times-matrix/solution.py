import numpy as np

def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    try:
	    return np.dot(a, b)
    except:
        return -1