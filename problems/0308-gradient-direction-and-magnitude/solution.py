import numpy as np

def gradient_direction_magnitude(gradient: list) -> dict:
	"""
	Calculate the magnitude and direction of a gradient vector.
	
	Args:
		gradient: A list representing the gradient vector
	
	Returns:
		Dictionary containing:
		- magnitude: The L2 norm of the gradient
		- direction: Unit vector in direction of steepest ascent
		- descent_direction: Unit vector in direction of steepest descent
	"""
	# Your code here
	grdDict = {}

	gradient = np.array(gradient).astype(float)

	grdDict['magnitude'] = np.sqrt(
		np.sum(
			gradient**2
	))

	if grdDict['magnitude'] == 0:
		grdDict['direction'] = [0.0, 0.0]
		grdDict['descent_direction'] = [0.0, 0.0]
		return grdDict

	grdDict['direction'] = list(gradient / grdDict['magnitude'])
	grdDict['descent_direction'] = list(np.negative(gradient / grdDict['magnitude']))

	return grdDict