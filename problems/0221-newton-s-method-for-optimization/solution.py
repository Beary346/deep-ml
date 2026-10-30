from typing import Callable
import numpy as np

def newtons_method_optimization(
    gradient_func: Callable[[list[float]], list[float]],
    hessian_func: Callable[[list[float]], list[list[float]]],
    x0: list[float],
    tol: float = 1e-6,
    max_iter: int = 100
) -> list[float]:
    x = np.array(x0, dtype=float)

    for i in range(max_iter):
        # Evaluate gradient and Hessian AT the current point x
        grad = np.array(gradient_func(x.tolist()), dtype=float)
        H = np.array(hessian_func(x.tolist()), dtype=float)

        # Check convergence: gradient norm is small enough
        if np.linalg.norm(grad) < tol:
            break

        # Newton step: x_new = x - H^{-1} @ grad
        x = x - np.linalg.inv(H) @ grad

    return x.tolist()   
