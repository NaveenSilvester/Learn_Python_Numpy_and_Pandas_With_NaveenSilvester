"""
Transpose of a Matrix
The transpose flips the matrix over its diagonal—rows become columns 
and vice versa. In NumPy, we use .T or np.transpose().
"""
import numpy as np
C = np.array([[1, 2, 3], [4, 5, 6]])

# Transpose using .T
transpose_C = C.T

# Alternative way
transpose_C_alt = np.transpose(C)

print("Original Matrix:\n", C)
print("Transpose of Matrix:\n", transpose_C)