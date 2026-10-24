import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y).reshape(-1, 1)
    theta = np.linalg.inv(X.T @ X) @ X.T @ y
    return np.round(theta, 4).flatten().tolist()