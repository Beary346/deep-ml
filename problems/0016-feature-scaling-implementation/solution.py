import numpy as np

def feature_scaling(data: np.ndarray) -> (np.ndarray, np.ndarray):
    # Your code here
    standardization = np.round((data - np.mean(data, axis=0)) / np.std(data, axis=0), 4)
    min_max = np.round((data - np.min(data, axis=0)) / (np.max(data, axis=0) - np.min(data, axis=0)), 4)

    return (standardization, min_max)
