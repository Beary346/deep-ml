import numpy as np

def make_diagonal(x):
    # Your code here
    arr = np.zeros((x.shape[-1], x.shape[-1]))
    for i in range(len(x)):
        arr[i][i] = x[i]
    
    return arr