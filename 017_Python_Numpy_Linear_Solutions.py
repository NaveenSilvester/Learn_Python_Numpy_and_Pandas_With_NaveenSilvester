"""
Linear Equations
Solving linear equations is a fundamental application of linear algebra, and NumPy 
provides a powerful function, numpy.linalg.solve(), to solve systems of linear equations efficiently.
Understanding Linear Equations
A system of linear equations can be written in matrix form as:
Ax=B
where:
•	A is the coefficient matrix,
•	x is the unknown variable vector,
•	B is the constant matrix.
To find x, we use:
x= A^{-1} B
However, instead of computing the inverse explicitly (which can be computationally expensive), 
NumPy provides numpy.linalg.solve() to directly solve for xx.

"""
print ("""
#######################################################################################################
       Example-1: Linear Solutions with two variables
#######################################################################################################       
""")
import numpy as np
# Define coefficient matrix A
A = np.array([[1,2],[3,5]])
# Define constant matrix B
B = np.array([1,2])
# Solve for x
x = np.linalg.solve(A, B)
print("Solution for x and y:", x)


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: Linear Solutions with three variables
#######################################################################################################       
""")
# Define coefficient matrix A
A = np.array([[2,1,-1], [-3,2,4], [-2,1,2]])
# Define constant matrix B
B = np.array([8, -11, -3])
# Solve for x, y, and z
solution = np.linalg.solve(A,B)
print(f"The solutions for x, y and z: {solution}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")