import numpy as np

def gaussian_elimination(A, b):
	"""
	Solves the system Ax = b using Gaussian Elimination with partial pivoting.
    
	:param A: Coefficient matrix
	:param b: Right-hand side vector
	:return: Solution vector x
	"""

	n = len(b)
	Ab = np.column_stack((A,b))
	for i in range(n):
		max_row = i + np.argmax(np.abs(Ab[i:,i]))
		if i!=max_row:
			Ab[[i,max_row]] = Ab[[max_row,i]]

		if Ab[i, i] == 0:
			raise ValueError("Matrix is singular or has no unique solution.")

		
		for j in range(i+1,n):
			factor = Ab[j,i]/Ab[i,i]
			Ab[j,i:] -= factor * Ab[i,i:]

		x = np.zeros(n)
		for i in range(n-1,-1,-1):
			x[i] = (Ab[i,-1]  - np.sum(Ab[i,i+1:n] * x[i+1:n]))/Ab[i,i]

	return x
