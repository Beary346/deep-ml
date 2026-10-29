import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    g_coeffs = np.array(g_coeffs)
    h_coeffs = np.array(h_coeffs)

    # Get the derivative of each 1d numpy array
    # Turn array into regular number problem 
    # Use np.polyder() and np.polyval
    g_ofx = np.polyval(g_coeffs, x)
    h_ofx = np.polyval(h_coeffs, x)

    g_prime_ofx = np.polyval(np.polyder(g_coeffs), x)
    h_prime_ofx = np.polyval(np.polyder(h_coeffs), x)

    quotient = ((g_prime_ofx * h_ofx) - (g_ofx * h_prime_ofx)) / (h_ofx ** 2)

    return round(quotient, 4)