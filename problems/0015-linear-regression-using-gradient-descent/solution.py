import numpy as np

def linear_regression_gradient_descent(X, y, alpha, iterations):
    m, n = X.shape
    y = y.reshape(-1, 1)
    theta = np.zeros((n, 1))

    for i in range(iterations):
        y_pred = X @ theta
        error = y_pred - y
        theta -= (alpha / m) * (X.T @ error)

    return theta.flatten()