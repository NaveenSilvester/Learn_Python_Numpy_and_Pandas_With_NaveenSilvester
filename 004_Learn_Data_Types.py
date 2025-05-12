import numpy as np
print(
"""
######################################################################################################
Understanding array data types
NumPy arrays are homogenous, meaning all elements must have the same data type. 
The dtype attribute in NumPy defines the type of elements stored in an array, ensuring efficient 
memory usage and optimized computations
######################################################################################################
"""
)

print ("""
#######################################################################################################
       Example-1 Checking Data Type
#######################################################################################################       
""")
list_data = [0,1,2,3,4,5,6,7,8,9,10,11]
numpy_array = np.array(list_data)
print (f"The NumPy Array numpy_array is: {numpy_array}")
print (f"The Data type of numpy_array numpy_array.dtype: {numpy_array.dtype}")
print (f"The Python Data type of numpy_array type(numpy_array): {type(numpy_array)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-2 Checking Data Type
#######################################################################################################       
""")
list_data = [0,1,2,3,4,5,6,7,8,9,10,11]
numpy_array = np.array(list_data, dtype=np.float64)
print (f"The NumPy Array numpy_array is: {numpy_array}")
print (f"The Data type of numpy_array numpy_array.dtype: {numpy_array.dtype}")
print (f"The Python Data type of numpy_array type(numpy_array): {type(numpy_array)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-3 Changing Data Type
#######################################################################################################       
""")
arr = np.array([1.0,2.0,3.0])
print (f"NumPy array arr contains : {arr}")
print (f"Numpy arrray arr is of data type arr.dtype: {arr.dtype}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-4 Changing Data Type
#######################################################################################################       
""")
arr = np.array([1.0,2.0,3.0])
print (f"NumPy array arr contains : {arr}")
print (f"Numpy arrray arr is of data type arr.dtype: {arr.dtype}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-5 Structured Data Type
#######################################################################################################       
""")
dt = np.dtype([('name', np.str_, 16), ('age', np.int32)])
arr = np.array([('Alice', 25),("Bob", 40)], dtype=dt)
print (f"NumPy array arr contains : {arr}")
print (f"Numpy arrray arr is of data type arr.dtype: {arr.dtype}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")