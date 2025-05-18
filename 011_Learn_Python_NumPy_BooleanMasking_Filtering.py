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

###########################################################################################################
### Play Book
###########################################################################################################

AA = np.array([1,2,3,4,5,6,7,8,9,10])
AA_2D = AA.reshape(2,5)

print (f"{AA.dtype} : DataType is {type(AA)} : Dimension is {AA.ndim} : shape is : {AA.shape} ")
print (f"AA_2D is {AA_2D} DataType is {type(AA_2D)} : Dimension is {AA_2D.ndim} : shape is : {AA_2D.shape} : ")


numpy_arr = np.arange(1,100,2)
auto_reshaped = numpy_arr.reshape(-1,10)
print (auto_reshaped)

print (f"AA is {AA}")
AA_slice = AA[1:5]
print (f"AA_slice is {AA_slice}")
print (f"AA > 2 : {AA[AA > 2]}")
AA_slice = 7
print (f"AA : {AA}")

print (f"AA : {AA}")


arr = np.array([1,2,3,4,5,6,7,8,9,10])
slice_arr = arr[1:4]
print (f"slice_arr: \n{slice_arr}\n")
print (f"arr: \n{arr}\n")
slice_arr[:] = 99
print (f"slice_arr: \n{slice_arr}\n")
print (f"arr: \n{arr}\n")

arr = np.array([1,2,3,1,5,6,7,8,9,10])
index = np.where(arr == 1)
print(f"Index is {index}")