"""
Copying vs View (memory optimization)
In NumPy, copying and viewing refer to different was of handling array data
Copy
A copy creates a new array with duplicated data
Changes made to the copy do not affect the original array
Copies are memory-intensive but necessary when independent modifications are required

View
A view provides a different perspective on the same data buffer.
Changes made to a view reflect in the original array.
Views are efficient as they avoid unnecessary memory duplication
You can create a view using ndarray.view()

"""
import numpy as np
print ("""
#######################################################################################################
       Example-1: Copy Array
#######################################################################################################       
""")
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print (f"Original Array arr consists of :\n{arr}")
x = arr.copy()
print (f"A copy of Array arr which is x= arr.copy looks like this:\n{x}")
arr[0] = 1000
print (f"Manipulated Array arr arr[0] = 100 looks like:\n{arr}")
print (f"Array x looks like this:\n{x}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: View Array
#######################################################################################################       
""")
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print (f"Original Array arr consists of :\n{arr}")
x = arr.view()
print (f"A view of Array arr which is x= arr.view looks like this:\n{x}")
arr[0] = 1000
print (f"Manipulated Array arr arr[0] = 100 looks like:\n{arr}")
print (f"Array x looks like this:\n{x}")
print(f"NOTE: The x is an array which is a view of original array arr, changes made in arr gets reflected in x too")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

a = np.arange(10)
print (f"The value of a is {a}")
a = 100
print (f"The new value of a is {a}")