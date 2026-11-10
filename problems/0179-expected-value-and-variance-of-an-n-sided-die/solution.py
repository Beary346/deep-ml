def dice_statistics(n: int) -> tuple[float, float]:
    """
    Compute the expected value and variance of a fair n-sided die roll.

    Args:
        n (int): Number of sides of the die

    Returns:
        tuple: (expected_value, variance)
    """
    # Your code here
    E = (n + 1) / 2 # Why is this the expected value?
    var = ((n**2) - 1) / 12 # Why is this the variance? 
    # Why are both of these divided, added, or subtraced by static numbers?
\
    return (E, var)