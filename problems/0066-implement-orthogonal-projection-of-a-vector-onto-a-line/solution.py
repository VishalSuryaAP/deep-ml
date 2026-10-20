
def orthogonal_projection(v, L):
	import numpy as np
	"""
	Compute the orthogonal projection of vector v onto line L.

	:param v: The vector to be projected
	:param L: The line vector defining the direction of projection
	:return: List representing the projection of v onto L
	"""
	v = np.array(v)
	L = np.array(L)
	vl = v @ L  
	ll = L @ L  
	proj = (vl/ll) * L  
	return proj
