"""
Dot Product (Matrix Multiplication)
The dot product of two matrices is their matrix multiplication. 
In NumPy, you can use np.dot() or @ (Python's matrix multiplication operator).
"""
import numpy as np
print ("""
#######################################################################################################
       Example-1: Dot PRODUCT
#######################################################################################################       
""")
# Define two matrices
A = np.array( [[1,2], [3,4]] )
B = np.array( [[5,6],[7,8]] )
# Compute dot product
dot_product = np.dot(A, B)
print("Dot product (Matrix Multiplication):\n", dot_product)
# Alternative way using @ operator
dot_product_alt = (A @ B)
print("Matrix A:\n", A)
print("Matrix B:\n", B)
print("Dot product Aleternative (Matrix Multiplication):\n", dot_product_alt)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")