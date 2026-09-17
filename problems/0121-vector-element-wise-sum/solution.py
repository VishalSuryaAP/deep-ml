def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) == len(b):
		result = []
		for i in range(len(a)):
			result.append(a[i]+b[i])
		return result
	else:
		return -1