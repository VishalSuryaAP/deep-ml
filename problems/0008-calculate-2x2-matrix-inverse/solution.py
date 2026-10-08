def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # 1. Unpack the elements for clean mathematical mapping
    a, b = matrix[0][0], matrix[0][1]
    c, d = matrix[1][0], matrix[1][1]
    
    # 2. Calculate the determinant
    det = a * d - b * c
    if det == 0:
        return None
    
    # 3. Apply the 2x2 inverse formula: (1/det) * [[d, -b], [-c, a]]
    inv_matrix = [
        [d / det, -b / det],
        [-c / det, a / det]
    ]
    
    return inv_matrix
