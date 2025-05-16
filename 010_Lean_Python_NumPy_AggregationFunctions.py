"""
Aggregation Functions in NumPy
Aggregation functions in NumPy allow you to perform statistical operations on array efficiently. These functions help summarize data by computing values such as sum, mean, max, min, standard deviation, variance and more

"""
print ("""
#######################################################################################################
       Example-1: Sum
#######################################################################################################       
""")
import numpy as np

A = np.array([
[1,2,3],
[4,5,6]
])
# Compute sum of all elements
total = np.sum(A)

# Compute sum along rows (axis = 1)
row_sum = np.sum(A, axis=1)

# Compute sum along columns (axis = 0)
col_sum = np.sum(A, axis=0)

print (f"Array A contains:\n {A}")
print (f"Total Sum: {total}")
print (f"Row Sum: {row_sum}")
print (f"Col Sum: {col_sum}") 
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: Mean
#######################################################################################################       
""")
import numpy as np

A = np.array([
[1,2,3],
[4,5,6]
])
# Compute sum of all elements
total_mean = np.mean(A)

# Compute sum along rows (axis = 1)
row_mean = np.mean(A, axis=1)

# Compute sum along columns (axis = 0)
col_mean= np.mean(A, axis=0)

print (f"Array A contains:\n {A}")
print (f"Total Mean: {total_mean}")
print (f"Row Mean: {row_mean}")
print (f"Col Mean: {col_mean}") 
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-3: Maximum (np.max) & Minimum (np.min)
#######################################################################################################       
""")
import numpy as np

A = np.array([
[1,2,3],
[4,5,6]
])
# Compute max & min of all elements
total_max = np.max(A)
total_min = np.min(A)

# Compute max & min along rows (axis = 1)
row_max = np.max(A, axis=1)
row_min = np.min(A, axis=1)

# Compute max & min along columns (axis = 0)
col_max= np.max(A, axis=0)
col_min= np.min(A, axis=0)

print (f"Array A contains:\n {A}")
print (f"Total Max: {total_max}")
print (f"Total Min: {total_min}")
print (f"Row Max: {row_max}")
print (f"Row Min: {row_min}")
print (f"Col Max: {col_max}") 
print (f"Col Min: {col_min}") 
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-4: Standard Deviation & Variation
#######################################################################################################       
""")
import numpy as np

A = np.array([
[1,2,3],
[4,5,6]
])
# Compute Std & Var of all elements
total_std = np.std(A)
total_var = np.var(A)

# Compute std & var along rows (axis = 1)
row_std = np.std(A, axis=1)
row_var = np.var(A, axis=1)

# Compute std & var along columns (axis = 0)
col_std= np.std(A, axis=0)
col_var= np.var(A, axis=0)

print (f"Array A contains:\n {A}")
print (f"Total STD: {total_std}")
print (f"Total VAR: {total_var}")

print (f"Row STD: {row_std}")
print (f"Row VAR: {row_var}")

print (f"Col STD: {col_std}") 
print (f"Col VAR: {col_var}") 
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-5: Median
#######################################################################################################       
""")
import numpy as np

A = np.array([
[1,2,3],
[4,5,6]
])
# Compute median of all elements
total_median = np.median(A)

# Compute median along rows (axis = 1)
row_median = np.median(A, axis=1)

# Compute median along columns (axis = 0)
col_median= np.median(A, axis=0)

print (f"Array A contains:\n {A}")
print (f"Total Median: {total_median}")
print (f"Row Median: {row_median}")
print (f"Col Median: {col_median}") 
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")