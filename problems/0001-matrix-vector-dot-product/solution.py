def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	# Return a list where each element is the dot product of a row of 'a' with 'b'.
	# If the number of columns in 'a' does not match the length of 'b', return -1.
	if len(a[0])!=len(b):
		return -1
	else:
		result = [0 for _ in range(len(a[0]))]
		for i in range(len(a)):
			tmp = 0
			for j in range(len(a[0])):
				tmp += (a[i][j] * b[j])
			result[i] = tmp
	return result
