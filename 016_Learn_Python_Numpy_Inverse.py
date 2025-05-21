"""
Inverse of a Matrix
The inverse of a square matrix A is another matrix A⁻¹ 
such that A * A⁻¹ = I (where I is the identity matrix). In NumPy, we use np.linalg.inv().
"""
import numpy as np
print ("""
#######################################################################################################
       Example-1: Inverse Matrix
#######################################################################################################       
""")
D = np.array([[4, 7], [2, 6]])

# Compute the transpose
Transpose_Matrix = np.transpose(D)
# Compute the inverse
inverse_D = np.linalg.inv(D)

print("Original Matrix:\n", D)
print("Transpose of Matrix:\n", Transpose_Matrix)
print("Inverse of Matrix:\n", inverse_D)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



