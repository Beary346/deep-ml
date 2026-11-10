import numpy as np

def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # TODO: Implement the function
    sample_size = len(samples)
    uniques, count = np.unique(samples, return_counts=True)

    lst = []
    for i, x in enumerate(uniques):
        lst.append((int(x), float(count[i]/sample_size)))
    
    return lst