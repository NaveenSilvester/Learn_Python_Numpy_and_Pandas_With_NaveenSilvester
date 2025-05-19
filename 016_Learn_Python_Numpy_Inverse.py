"""
Inverse of a Matrix
The inverse of a square matrix A is another matrix A⁻¹ 
such that A * A⁻¹ = I (where I is the identity matrix). In NumPy, we use np.linalg.inv().
"""
import numpy as np
D = np.array([[4, 7], [2, 6]])

# Compute the transpose
Transpose_Matrix = np.transpose(D)
# Compute the inverse
inverse_D = np.linalg.inv(D)

print("Original Matrix:\n", D)
print("Transpose of Matrix:\n", Transpose_Matrix)
print("Inverse of Matrix:\n", inverse_D)




# Define coefficient matrix A
A = np.array([[2,1,-1], [-3,2,4], [-2,1,2]])
# Define constant matrix B
B = np.array([8, -11, -3])
# Solve for x, y, and z
solution = np.linalg.solve(A,B)
print(f"The solutions are: {solution}")