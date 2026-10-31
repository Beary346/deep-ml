import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
    """
    Calculate the magnitude and direction of a gradient vector.
    """
    g = np.array(gradient, dtype=float)
    magnitude = np.linalg.norm(g)

    if magnitude == 0:
        return {
            "magnitude": 0.0,
            "direction": [0.0, 0.0],
            "descent_direction": [0.0, 0.0],
        }

    direction = g / magnitude
    return {
        "magnitude": float(magnitude),
        "direction": direction.tolist(),
        "descent_direction": (-direction).tolist(),
    }