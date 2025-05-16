"""
                                    Broadcasting in NumPy
Broadcasting in NumPy refers to the ability of NumPy to perform element-wise operations 
on arrays of different shapes without the need for explicit looping. This feature 
allows for efficient computation and memory usage, making operations faster compared to 
traditional looping approaches.

How Broadcasting works (Step-by-Step Explanation)
1.	Understanding the Rules: Broadcasting follows specific rules to match arrays of 
    different shapes:
    •	The arrays are aligned starting from the rightmost dimension
    •	If dimensions differ, the smaller array is expanded by repeating its values.
    •	A dimension with size 1 can be stretched to match the corresponding dimension
        of the larger array
2.	Compatible Shapes: Two arrays can be broadcast together only if:
    •	They have the same shape
    •	The shape of one of the arrays is 1 in a dimension that differs
3.	Applying Broadcasting: Instead of manually reshaping and repeating arrays NumPy 
        automatically extends the smaller array to match the larger array during operations.

"""

print ("""
#######################################################################################################
       Example-1: Addition of Matrix
#######################################################################################################       
""")
import numpy as np

# Create a 2D Arary of dimeansion (3x3)
A = np.array([
   [1,2,3],
   [4,5,6],
   [7,8,9] 
])

# Create a 1D Arary of dimeansion (1x3)
B = np.array([10,20,30])

# Matrix addition between A and B
result = A + B

C = np.array([[1,2,3]])
AandC = A + C


print(f"The Matrix A is:\n {A}")
print(f"The Dimension of A is: {A.ndim}")
print(f"The Shape of A is: {A.shape}")
print(f"The Matrix B is:\n {B}")
print(f"The Dimension of B is: {B.ndim}")
print(f"The Shape of B is: {B.shape}")
print("Adding Matrix A and Matrix B")
print (f"The result of adding Matrix A and B is: \n {result}\n")

print(f"The Matrix A is:\n {A}")
print(f"The Dimension of A is: {A.ndim}")
print(f"The Shape of A is: {A.shape}\n")
print(f"The Matrix C is:\n {C}")
print(f"The Dimension of C is: {C.ndim}")
print(f"The Shape of C is: {C.shape}")
print("Adding Matrix A and Matrix C")
print (f"The result of adding Matrix A and C is: \n {AandC}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: Scalar Addition of Matrix
#######################################################################################################       
""")
# Define a 2D Array
A = np.array([
    [1,2,3],
    [4,5,6]])
# Scalar addition with 10
result = A + 10
print (f"Matrix A containes: \n{A}")
print ("Scalar addition with 10")
print (f"Scalar addition of A with 10:\n{result}"
)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: Broadcasting with 1D and 2D Arrays
#######################################################################################################       
""")
# Define a 2D array
B = np.array([[10],[20]]) # Shape (2,1)
C = np.array([1,2,3]) # Shape(1,3)
result = B + C # Broadcasting applied
print (f"Array A containes: \n{A}")
print (f"Array A Dimension: \n{A.ndim}")
print (f"Array A shape: \n{A.shape}")

print (f"Array C containes: \n{C}")
print (f"Array C Dimension: \n{C.ndim}")
print (f"Array C shape: \n{C.shape}")
print ("Addition and B and C")
print (f"Addition of A with C:\n{result}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-3: Broadcasting with Element-wise Multiplication
NOTE: Explanation: Y is expanded vertically to match X.
#######################################################################################################       
""")
X = np.array([
    [1,2,3],
    [4,5,6]
    ])

Y = np.array([10,20,30])
result = X * Y

print (f"Array X containes: \n{X}")
print (f"Array X Dimension: \n{X.ndim}")
print (f"Array X shape: \n{X.shape}")

print (f"Array Y containes: \n{Y}")
print (f"Array Y Dimension: \n{Y.ndim}")
print (f"Array Y shape: \n{Y.shape}")
print ("Multiplication and X and Y")
print (f"Multiplication of X with Y:\n{result}")
print ("""
Explanation: Y is expanded vertically to match X.
""")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-5: Broadcasting Across Higher Dimensions
#######################################################################################################       
""")
D = np.ones((3,1,2))
E = np.array([5,10])
result = D * E


print (f"Array D containes: \n{D}")
print (f"Array D Dimension: \n{D.ndim}")
print (f"Array D shape: \n{D.shape}")

print (f"Array E containes: \n{E}")
print (f"Array E Dimension: \n{E.ndim}")
print (f"Array E shape: \n{E.shape}")
print ("Multiplication and D and E")
print (f"Multiplication of D with E:\n{result}")
print ("""
Explanation: E expands to match the second dimension of D.
""")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")