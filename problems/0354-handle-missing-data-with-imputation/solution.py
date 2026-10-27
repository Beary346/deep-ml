import numpy as np

def impute_missing_data(data: np.ndarray, strategy: str = 'mean') -> np.ndarray:
    """
    Impute missing values in a 2D array using the specified strategy.
    
    Args:
        data: 2D numpy array with missing values represented as np.nan
        strategy: Imputation strategy - 'mean', 'median', or 'mode'
        
    Returns:
        2D numpy array with missing values imputed
    """
    # Your code here
    for i in range(data.shape[-1]):
        column = data[:, i]
        if np.isnan(column).any(): # If any value in current column is Nan...
            location = np.where(np.isnan(column))[0] # Get the row location of all values that are Nan.
            if strategy == 'mean':
                data[location, i] = np.nanmean(column)
            elif strategy == 'median':
                data[location, i] = np.nanmedian(column)
            else:  # mode
                valid = column[~np.isnan(column)].astype(int)
                data[location, i] = np.argmax(np.bincount(valid))
    return data