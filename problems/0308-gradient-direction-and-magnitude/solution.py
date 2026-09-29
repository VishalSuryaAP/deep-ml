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
	gradient  = np.array(gradient)
	magnitude = np.linalg.norm(gradient)
	if magnitude == 0:
		direction = [0 for _ in range(len(gradient))]
		desent_direction = [0 for _ in range(len(gradient))]
		return {"magnitude":magnitude,
			"direction":direction,
			"descent_direction":desent_direction}
	direction = [x/magnitude for x in gradient]
	desent_direction = [-x for x in direction]

	return {"magnitude":magnitude,
			"direction":direction,
			"descent_direction":desent_direction}

