def matrixmul(a:list[list[int|float]],
              b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0])!=len(b):
        return -1
    m = len(a)
    n = len(a[0])
    p = len(b[0])
    C = [[0 for row in range(p)] for col in range(m)]
    for i in range(m):
        for j in range(p):
            for k in range(n):
                C[i][j] += a[i][k] * b [k][j]
        
    return C

