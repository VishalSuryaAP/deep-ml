import numpy as np

def matrix_rank(A: np.ndarray, tol: float = 1e-10) -> int:
    """
    Compute the rank of a matrix.
    
    Args:
        A: Input matrix of shape (m, n)
        tol: Tolerance for considering values as zero
    
    Returns:
        The rank of the matrix (integer)
    """
    M = A.astype(float).copy()
    num_rows, num_cols = M.shape
    rank = 0
    pivot_row = 0
    
    for col in range(num_cols):
        if pivot_row >= num_rows:
            break
            
        # Find the row with the maximum absolute value in this column (pivoting)
        max_row = pivot_row + np.argmax(np.abs(M[pivot_row:, col]))
        
        # If the pivot is zero (or very close), skip this column
        if np.abs(M[max_row, col]) < 1e-9:
            continue
        
        # Swap rows to bring the pivot up
        M[[pivot_row, max_row]] = M[[max_row, pivot_row]]
        
        # Eliminate the values below the pivot
        for r in range(pivot_row + 1, num_rows):
            factor = M[r, col] / M[pivot_row, col]
            M[r, col:] -= factor * M[pivot_row, col:]
            
        rank += 1
        pivot_row += 1
    return rank

        

    