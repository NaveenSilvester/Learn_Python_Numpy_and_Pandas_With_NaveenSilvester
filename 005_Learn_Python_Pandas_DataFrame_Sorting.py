"""
Pandas DataFrame Manipulation and Cleaning
Data manipulation and cleaning are critical steps in data analysis, and Python's 
Pandas library is a powerful tool for these tasks.
Data cleaning involves handling missing values, removing duplicates, correcting 
data types, and dealing with inconsistencies.

Data Manipulation Methods
Data manipulation involves filtering, sorting, grouping, merging, and reshaping data.

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
       Example-1: Sorting Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nSorting the DataFrame with descending order of their salary")
print(f"{df.sort_values("Salary", ascending=False)}")        
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

