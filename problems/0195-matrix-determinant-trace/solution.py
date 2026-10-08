def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
    """
    Compute the determinant and trace of a square matrix.
    
    Args:
        matrix: A square matrix (n x n) represented as list of lists
    
    Returns:
        Tuple of (determinant, trace)
    """
    # 1. Handle edge cases for empty matrices or 1x1 matrices
    n = len(matrix)
    if n == 0 or len(matrix[0]) == 0:
        return (0.0, 0.0)
    
    if n == 1:
        return (float(matrix[0][0]), float(matrix[0][0]))

    # Helper function to get the submatrix (minor)
    def get_matrix_minor(mat, i, j):
        return [row[:j] + row[j+1:] for row in (mat[:i] + mat[i+1:])]

    # Helper recursive function to calculate the determinant
    def determinant(mat):
        size = len(mat)
        # Base case for 1x1 matrix inside recursion
        if size == 1:
            return mat[0][0]
        # Base case for 2x2 matrix
        if size == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
        
        det_val = 0
        for c in range(size):
            sign = (-1) ** c  # Parentheses are required around -1
            minor = get_matrix_minor(mat, 0, c)
            det_val += sign * mat[0][c] * determinant(minor)
        return det_val

    # 2. Compute the trace (sum of the main diagonal elements)
    trace = sum(matrix[i][i] for i in range(n))
    
    # 3. Compute the determinant
    det = determinant(matrix)

    return (float(det), float(trace))
