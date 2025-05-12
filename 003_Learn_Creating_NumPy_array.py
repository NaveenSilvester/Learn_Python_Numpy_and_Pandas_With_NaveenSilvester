import numpy as np
print(
"""
######################################################################################################
Different ways of Creating NumPy Arrays
NumPy provides several ways to create arrays, each suited to different use cases.
        np.array() : This is the most basic way to create a NumPy array using Python list or tuples
        np.arange() : This function creates arrays with evenly spaced values
        np.linspace() : Generates a specified number of evenly spaced values between a given range.
        np.zero() : Create arrays filled with zeros or ones
        np.ones() : Create arrays filled with zeros or ones
        np.full() : Creates an array filled with specific values
        np.eye() : Generates an identity matrix
        np.random() : Creates arrays filled with random values
        np.empty() : Creates an uninitialized array (contains garbage values)
######################################################################################################
"""
)

print ("""
#######################################################################################################
       Example-1 Using np.array()
       •	np.array() converts a list or tuple into NumPy array
       •	It automatically determines the data type (dtype) of elements
#######################################################################################################       
""")
list_data = [0,1,2,3,4,5,6,7,8,9,10,11]
numpy_array = np.array(list_data)
print (f"Python list list_data: {list_data}")
print (f"NumPy array numpy_array from list_data: {numpy_array}")
print (f"Data Type of numpy_array: {type(numpy_array)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2 Using np.arange()
       •	This function creates arrays with evenly spaced values
#######################################################################################################       
""")

numpy_array_arange = np.arange(10)
print (f"A NumPy array created using np.arange(10): {numpy_array_arange}")
print (f"Data Type of numpy_array_range: {type(numpy_array_arange)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-3 Using np.linspace()
       •	Generates a specified number of evenly spaced values between a given range.
       •	np.linspace(start, stop, num_elements) ensures precision when dividing a range into equal parts
       •	Often used in plotting or mathematical computations
#######################################################################################################       
""")

numpy_array_linspace = np.linspace(0,10,5)
print (f"A NumPy array created using np.linspace(0,10,5): {numpy_array_linspace}")
print (f"Data Type of numpy_array_linspace: {type(numpy_array_linspace)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-4 Using np.zeros()
       •	Create arrays filled with zeros.
       •	np.zeros(shape) creates an array filled with zeros
#######################################################################################################       
""")

numpy_array_zeros = np.zeros((3,5))
print (f"A NumPy array created using np.zeros((3,5)): \n{numpy_array_zeros}")
print (f"Data Type of numpy_array_zeros: {type(numpy_array_zeros)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-5 Using np.ones()
       •	Create arrays filled with zeros.
       •	np.ones(shape) creates an array filled with zeros
#######################################################################################################       
""")

numpy_array_ones = np.ones((3,5))
print (f"A NumPy array created using np.ones((3,5)): \n{numpy_array_ones}")
print (f"Data Type of numpy_array_ones: {type(numpy_array_ones)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-6 Using np.full()
       •	Creates an array filled with specific values.
       •    np.full(shape, value) creates an array with a predefined value
#######################################################################################################       
""")

numpy_array_full = np.full((3,5),7)
print (f"A NumPy array created using np.full((3,5),7): \n{numpy_array_full}")
print (f"Data Type of numpy_array_full: {type(numpy_array_full)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-7 Using np.eye()
       •	Creates an identity matrix
       •    Identity matrices are often used in linear algebra operations
#######################################################################################################       
""")

numpy_array_identity = np.eye(5)
print (f"A NumPy array created using np.identity(5): \n{numpy_array_identity}")
print (f"Data Type of numpy_array_identity: {type(numpy_array_identity)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")




print ("""
#######################################################################################################
       Example-8 Using np.random.rand()
       •	Creates arrays filled with random values
#######################################################################################################       
""")

numpy_array_random = np.random.rand(3,3)
numpy_array_random = np.random.rand(3,3)

print (f"A NumPy array created using np.random((3,5)): \n{numpy_array_random}")
print (f"Data Type of numpy_array_random: {type(numpy_array_random)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-9 Using np.empty()
       •	Creates an uninitialized array (contains garbage values).
#######################################################################################################       
""")


numpy_array_empty = np.empty((3,4))

print (f"A NumPy array created using np.empty((3,4)): \n{numpy_array_empty}")
print (f"Data Type of numpy_array_empty: {type(numpy_array_empty)}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")