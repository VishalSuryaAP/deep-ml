import numpy as np

def is_linearly_independent(vectors: list[list[float]]) -> bool:
    """
    Check if a set of vectors is linearly independent.
    
    Args:
        vectors: List of vectors, where each vector is a list of floats.
                 All vectors must have the same dimension.
        
    Returns:
        True if vectors are linearly independent, False otherwise.
    """
    # Your code here
    if not vectors:
        return True
    
    matrix = [list(v) for v in vectors]
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if num_rows>num_cols:
        return False

    rank = 0
    current_col = 0
    for r in range(num_rows):
        while current_col<num_cols:
            pivot_row = r 
            while pivot_row<num_rows and abs(matrix[pivot_row][current_col]) < 1e-9:
                pivot_row+=1
            if pivot_row<num_rows:
                matrix[r], matrix[pivot_row] = matrix[pivot_row], matrix[r]
                break
            current_col+=1
        if current_col>=num_cols:
            break
        pivot = matrix[r][current_col]
        for i in range(r+1,num_rows):
            factor = matrix[i][current_col] / pivot
            for j in range(current_col,num_cols):
                matrix[i][j] -= factor * matrix[r][j]
            
        rank+=1
        current_col+=1
    return rank == num_rows

