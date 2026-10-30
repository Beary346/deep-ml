import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    arr = np.array(arr, dtype=float)
    match norm_type:
        case 'l1':
            return float(np.sum(np.abs(arr)))
        case 'l2':
            return float(np.sqrt(np.sum(arr ** 2)))
        case 'linf':
            return float(np.max(np.abs(arr)))
        case 'frobenius':
            if arr.ndim != 2:
                raise ValueError('frobenius norm requires a 2D array')
            return float(np.sqrt(np.sum(arr ** 2)))
        case _:
            raise ValueError(f'Unknown norm type: {norm_type}')   