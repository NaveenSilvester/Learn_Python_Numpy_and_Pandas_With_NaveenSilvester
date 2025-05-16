"""
Boolean Masking and Filtering in NumPy
Boolean masking and filtering in NumPy allows you to select, modify or filter elements in an array based on a specific conditions. This technique is widely used in data analysis, machine learning and scientific computing.

Understanding Boolean Masks
A Boolean mask is a NumPy array containing True/False values that correspond to each element in another array. The True values indicate which elements should be selected.

Filtering Elements Using Boolean Mask
You can use the Boolean mask to filter elements from the array
"""
import numpy as np
print ("""
#######################################################################################################
       Example-1: Boolean Masking
#######################################################################################################       
""")
A = np.array([1,5,10,25,190,50, 71,20])
A_bool = A > 50
print (f"Elements for A : {A}")
print (f"Masking elements of A that are > 50 {A_bool}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-2: Filtering Elements Using Boolean Mas
#######################################################################################################       
""")
A = np.array([1,5,10,25,190,50, 71,20])
A_bool = A > 50

print (f"Elements for A : {A}")
print (f"Filtering elements of A that are > 50 : {A[A > 50]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-3: Filtering Odd Number from an array
#######################################################################################################       
""")
A = np.array([1,5,10,25,190,50, 71,20])
A_bool = A > 50
print (f"Elements for A : {A}")
print (f"Filtering elements of A that are > 50 : {A[A % 2 != 0]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-4: Filtering based on multiple condition
#######################################################################################################       
""")
A = np.array([1,5,10,25,190,50, 71,20])
print (f"Elements for A : {A}")
print (f"Filtering elements of A that are > 20  and are even: {(A[A > 20])}")
print (f"Filtering elements of A that are > 20  and are even: {A[(A %2 == 0) & (A > 20)]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")