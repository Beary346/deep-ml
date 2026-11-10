import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    if type(data) != np.ndarray:
        data = np.array(data)
    
    descriptions = {}

    descriptions['mean'] = np.mean(data)
    descriptions['median'] = np.median(data)

    vals, counts = np.unique(data, return_counts=True)
    descriptions['mode'] = vals[counts==np.max(counts)][0]

    descriptions['variance'] = np.sum((data - descriptions['mean'])**2) / data.shape[-1]

    descriptions['standard_deviation'] = np.sqrt(descriptions['variance'])

    p25, p50, p75 = np.percentile(data, [25, 50, 75])
    descriptions['25th_percentile'] = p25
    descriptions['50th_percentile'] = p50
    descriptions['75th_percentile'] = p75

    descriptions['interquartile_range'] = descriptions['75th_percentile'] - descriptions['25th_percentile']

    return descriptions