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

print ("""
#######################################################################################################
       Example-4 Filling Missing Values
       Using: fillna()
       Use fillna() to replace missing values with a specific value, mean, median or 
       forward/backward fill.
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
# Fill missing Age with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("After filling missing Age with mean:")
print(df)
# Fill missing Name with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')
print("\nAfter filling missing Name with 'Unknown':")
print(df)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-5 Intrapolating Missing Salary Values
       Using: interpolate() 
Use interpolate() for linear interpolation of numeric data.
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
# Fill missing Age with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].interpolate())
print("After filling missing Age with mean and Salary with interpolate:")
print(df)
# Fill missing Name with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')
print("\nAfter filling missing Name with 'Unknown':")
print(df)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-6 Removing Duplicate records
       Using: drop_duplicates()
Use drop_duplicates() to remove duplicate rows.
#######################################################################################################       
""")
df = pd.concat([df, df.iloc[[0]]], ignore_index=True)
print("DataFrame with duplicate row:")
print(df)
noduplicates_df = df.drop_duplicates()
print("\nData Frame with no Duplicate Records")
print(noduplicates_df)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-7 Correcting Data Types
       Using: astype() or pd.to_numeric()
Use astype() or pd.to_numeric() to ensure correct data types.
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
# Convert Age to integer
df['Age'] = df['Age'].astype(int)
print("\nAfter converting Age to integer:")
print(df)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")