def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	m,n = len(matrix),len(matrix[0])
	result = []
	if mode=='row':
		for i in range(m):
			tmp =0
			for j in range(n):
				tmp += matrix[i][j]
			result.append(tmp/n)

	if mode == 'column':
		for j in range(n):
			tmp = 0
			for i in range((m)):
				tmp+=matrix[i][j]
			result.append(tmp/m)


	return result