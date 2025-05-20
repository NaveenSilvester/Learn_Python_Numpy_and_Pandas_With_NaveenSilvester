"""
What are Eigenvalues and Eigenvectors?
Imagine a matrix as a machine that takes a vector (a list of numbers, like an arrow in space)
 and transforms it by stretching, shrinking or rotating it. An Eigenvector is a special vector
   that, when the matrix transforms it, doesn’t change its direction – it only gets scaled 
   (stretched or shrunk) by a number called eigenvalue.

Eigenvector: A Non-Zero vector that stays along the same line after the matrix transformation.
Eigenvalue: The number that tells you how much the eigenvector is scaled (stretched or shrunk).

"""
import numpy as np
print ("""
#######################################################################################################
       Example-1: Eigenvalues and Eigenvectors
#######################################################################################################       
""")
# Step 1: Create a square matrix
A = np.array([
    [4,2],
    [1,3]
    ])

# Step 2: Calculate eigenvalues and eigenvectors
eigenvalues, eigenvectors = np.linalg.eig(A)

# Step 3: Display results
print("Matrx A:\n", A)
print("\nEigenvalues:", eigenvalues)
print("\nEigenvectors:\n", eigenvectors)

# Step 4: Verification
print("\nVerification:")
for i in range(len(eigenvalues)):
    λ = eigenvalues[i]
    v = eigenvectors[:, i]
    print(f"\nFor eigenvalue λ={λ}:")
    print("A * v:", np.dot(A, v))
    print("λ * v:", λ * v)
    print("Are they equal?", np.allclose(np.dot(A, v), λ * v))

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
