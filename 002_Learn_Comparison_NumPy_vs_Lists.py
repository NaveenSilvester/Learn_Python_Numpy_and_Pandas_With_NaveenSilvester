print (""" 
######################################################################
#####     Speed Comparison between NumPy vs Python Lists         #####
######################################################################
""")
import numpy as np
import time

# Creating large list and NumPy array
list_data = list(range(1000000))
numpy_array = np.arange(1000000)

# Timing list operations
start = time.time()
list_result = [x * 2 for x in list_data] # using list comprehension
end = time.time()
print(f"List computation time: {end - start:.5f} seconds")

# Timing NumPy array operations
start = time.time()
numpy_result = numpy_array * 2 # vectorized operation
end = time.time()
print(f"NumPy computation time: {end - start: .5f} seconds")

print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

print("""
######################################################################
#####  Memory utilization Comparison between NumPy vs Python List ####
######################################################################
""")
import numpy as np
import sys

# Creating a Python list and a NumPy array with the same elements
python_list = [i for i in range(1000)]
numpy_array = np.arange(1000)

# Checking memory usage
python_list_size = sys.getsizeof(python_list) + sum(sys.getsizeof(i) for i in python_list)
numpy_array_size = numpy_array.nbytes

print(f"Memory used by Python list: {python_list_size} bytes")
print(f"Memory used by NumPy array: {numpy_array_size} bytes")
print ("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")