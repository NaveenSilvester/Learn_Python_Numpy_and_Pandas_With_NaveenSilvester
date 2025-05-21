"""
Pandas DataFrame Manipulation and Cleaning
Data manipulation and cleaning are critical steps in data analysis, and Python's 
Pandas library is a powerful tool for these tasks.
Data cleaning involves handling missing values, removing duplicates, correcting 
data types, and dealing with inconsistencies.

In Python, NaN (Not a Number) and None serve different purposes, but both can 
indicate missing values depending on the context.

Attribute	NaN (Not a Number)	None
Type	float (from NumPy/Pandas)	NoneType
Usage	Used in numerical computations	Represents a null or missing value
Behavior in Pandas	Recognized as a missing value	Also treated as missing, but converted to NaN in numerical columns
Mathematical Operations	Propagates (e.g., NaN + 5 = NaN)	Throws an error (e.g., None + 5 raises TypeError)
Checking for Missing Values	Use pd.isna() or np.isnan()	Use is None or pd.isna()
"""

import pandas as pd
import numpy as np

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 30, 22, 28],
    'Salary': [50000, 60000, np.nan, 45000, 52000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR']
}
df = pd.DataFrame(data)
print("Creating a sample DataFrame with missing values and None etc.,")
print("Original DataFrame:")
print(df)

print ("""
#######################################################################################################
       Example-1: Handling Missing Values
       Using: isna() or isnull()
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nDataFrame with is.na\n{df.isna()}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: Handling Missing Values
       Using: isnull()
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nDataFrame with is.null\n{df.isnull()}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-3 Dropping Missing Values
       Using: dropna()
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
df_dropped = df.dropna()
print("\nAfter dropping rows with missing values:")
print(df_dropped)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")