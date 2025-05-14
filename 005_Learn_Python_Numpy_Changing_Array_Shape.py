import numpy as np
print(
"""
######################################################################################################
UChanging array shape
NumPy provides several ways to reshape arrays, allowing you to modify their dimensions without 
changing the underlying data. This is useful for organizing data efficiently in scientific computing 
and machine learning.
.reshape()
.ravel() OR .flatten()
.transpose()
.resize()
using -1
######################################################################################################
"""
)

print ("""
#######################################################################################################
       Example-1: .reshape()
#######################################################################################################       
""")
list_data = [0,1,2,3,4,5,6,7,8,9,10,11]
numpy_array = np.array(list_data)
print (f"DAta type is {type(numpy_array)}")
print (f"Numpy dtyps is {numpy_array.dtype}")
numpy_array = numpy_array.reshape(3,4)
print (f"Reshaping numpy_arary to dimension 3,4: \n{numpy_array}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-2: .reshape()
#######################################################################################################       
""")
list_data = [0,1,2,3,4,5,6,7,8,9,10,11]
numpy_array = np.array(list_data)
print (f"DAta type is {type(numpy_array)}")
print (f"Numpy dtyps is {numpy_array.dtype}")
numpy_array = numpy_array.reshape(3,4)
print (f"Reshaping numpy_arary to dimension 3,4: \n{numpy_array}")
print ("Flattening the numpy_array")
print (f"The flattend numpy_array (numpy_array.ravel()) is : {numpy_array.ravel()}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-3: .transpose()
#######################################################################################################       
""")
list_data = [0,1,2,3,4,5,6,7,8,9,10,11]
numpy_array = np.array(list_data)
print (f"DAta type is {type(numpy_array)}")
print (f"Numpy dtyps is {numpy_array.dtype}")
numpy_array = numpy_array.reshape(3,4)
print (f"Reshaping numpy_arary to dimension 3,4: \n{numpy_array}")
print ("Transposing the numpy_array")
print (f"The Transpose numpy_array (numpy_array.transpose()) is :\n {numpy_array.transpose()}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-4: .resize()
       Unlike .reshape(), .resize() modifies the original array
    •	.resize(new_shape) changes the array in place.
    •	If the new shape is larger, NumPy fills extra spaces with 0.

#######################################################################################################       
""")
#list_data = [0,1,2,3,4,5,6,7,8,9,10,11]
#numpy_array = np.array(list_data)
arr = np.arange(12) #Output: [0,1,2,3,4,5,6,7,8,9,10,11]
print(f"The NumPy Array is : {arr}")
numpy_array_reshape = numpy_array.reshape(3,4)
print (f"The reshaping of NumPy Array numpy_array.reshape(3,4): \n {numpy_array_reshape}")
print (f"The original arr is : {arr}")
arr.resize(4,3)
print (f"The original arr after resize is :\n {arr}")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-5: Using -1 for Automatic Reshaping
NumPy can infer one dimension automatically
When you specify -1 as a dimension, NumPy automatically calculates that dimension based on the total 
number of elements
It ensures that the total number of elements remains the same after reshaping
#######################################################################################################       
""")
numpy_arr = np.arange(12)
# Reshaping into 2D with 6 columns
auto_reshaped = numpy_arr.reshape(-1,6)
print(auto_reshaped)


print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")