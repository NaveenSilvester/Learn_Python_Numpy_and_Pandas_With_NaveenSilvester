"""
                    Apply, Map, and ApplyMap

apply()
The apply function in pandas is used to apply a function along an axis 
of a DataFrame or on a Series. It’s a flexible way to perform custom operations 

map()
The map function in pandas is used to apply a function to each element in a Series. 
It’s similar to the apply function for a Series but is specifically designed for 
element-wise transformations and is often more efficient. Unlike DataFrame.apply, 
which can operate on rows or columns, map is limited to Series and is typically used 
for simple transformations or mapping values to new ones using a dictionary or 
function.

applymap()
The applymap() function in pandas is used to apply a function to every single element
 in a DataFrame. It's similar to map() for Series, but works on entire DataFrames.

"""


import numpy as np
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 30, 22, 28],
    'Salary': [50000, 60000, np.nan, 45000, 52000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR']
}
df = pd.DataFrame(data)
print(f"Original Dataframe is:\n{df}")


print ("""
#######################################################################################################
       Example-1: Apply
 apply()
The apply function in pandas is used to apply a function along an axis 
of a DataFrame or on a Series. It’s a flexible way to perform custom operations       
#######################################################################################################       
""")

df['Salary_Increased'] = df['Salary'].apply(lambda x: x * 1.1)
print("DataFrame with increased Salary:")
print(df)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: map()
The map function in pandas is used to apply a function to each element in a Series. 
It’s similar to the apply function for a Series but is specifically designed for 
element-wise transformations and is often more efficient. Unlike DataFrame.apply, 
which can operate on rows or columns, map is limited to Series and is typically used 
for simple transformations or mapping values to new ones using a dictionary or 
function.
#######################################################################################################       
""")
# Sample Series
data = pd.Series(['A', 'B', 'C', 'A'])
# Dictionary for mapping
grade_map = {'A': 'Excellent', 'B': 'Good', 'C': 'Average'}
# Apply map to replace values
result = data.map(grade_map)
print(result)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-3: map()

#######################################################################################################       
""")

import pandas as pd
# Sample Series
scores = pd.Series([85, 60, 95])
print(f"Original Series: \n{scores}")
# Function to categorize scores
def grade(score):
    if score >= 90:
        return 'A-Excellent'
    elif score >= 70:
        return 'B-Good'
    else:
        return 'C-Average'
# Apply the grade function using map
print(f"Mapping Scores to Grades:\n>=90: A-Excellent\n>=70 B-Good\n<70: C-Average")
result = scores.map(grade)
print(result)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-4: map()
       Handling NaN Values with na_action
#######################################################################################################       
""")
# Sample Series with NaN
data = pd.Series([1, 2, np.nan, 4])
# Function to square a number
def square(x):
    return x ** 2
# Apply map with na_action='ignore'
result = data.map(square, na_action='ignore')
print(result)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-5: map()
       You can use map to transform strings in a Series.
#######################################################################################################       
""")
# Sample Series with NaN
names = pd.Series(['alice', 'bob', 'charlie'])
print(f"Names of the team members:\n{names}")
# Capitalize the names
result = names.map(str.capitalize)
print(result)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-6: applymap()
The applymap() function in pandas is used to apply a function to every single element
 in a DataFrame. It's similar to map() for Series, but works on entire DataFrames.
#######################################################################################################       
""")
import pandas as pd
import numpy as np
# Create a sample DataFrame
data = {
    'A': [1.23, 4.56, 7.89],
    'B': [9.87, 6.54, 3.21],
    'C': [0.12, 3.45, 6.78]
}
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)
rounded_df = df.applymap(lambda x: round(x, 1))
print("\nRounded DataFrame:")
print(rounded_df)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
