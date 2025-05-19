"""
Searching for elements in Arrays using NumPy
Searching involves finding specific values or indices.
Finding an Element’s Index: 
    The np.where() function returns the index where the element is found.
Searching with Conditions:
    You can use conditions to filter elements.
Checking for an Element's Existence:
    np.isin() checks for the presence of a value.
"""
import numpy as np

print ("""
#######################################################################################################
       Example-1: Finding an Element's Index
#######################################################################################################       
""")
A = np.array([1,5,50,25,190,50, 71,20])
print (f"Elements for A : {A}")
index = np.where(A == 50)
print (f"The index of element 50 in array A is : {np.where(A == 50)} and index is {index[0]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-2: Find all elements greater than 25
#######################################################################################################       
""")
A = np.array([1,5,50,25,190,50, 71,20])
print (f"Elements for A : {A}")
index = np.where(A > 50)
print (f"The index of element 50 in array A is : {np.where(A == 50)} and index is {index[0]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-3: Checking for an Element's Existence
#######################################################################################################       
""")
A = np.array([1,5,50,25,190,50, 71,20])
print (f"Elements for A : {A}")
exists = np.isin(A, 50)
print (f"The element 50 is iin array A : {np.isin(A, 50)} : Their valus is {np.where(np.isin(A, 50))}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

#################################################################################################################
## Playbook
#################################################################################################################

def custom_fun(x):
 	return x**2 + 2*x + 1
# Create and Array
arr = np.array([1,2,3,4]) 
# Apply function using np.vectorize()
vectorized_func = np.vectorize(custom_fun)
result = vectorized_func(arr)
print(result) 


arr2 = np.array([1,2,3,4])
print (arr2 ** 2 + 2* arr2 + 1)