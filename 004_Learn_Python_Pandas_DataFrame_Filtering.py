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
       Example-1: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"Filtering records where the salary of individuals are > 5000")
print (df[df["Salary"]>45000])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"Filtering records where the Department of individuals is HR")
print (df[df["Department"] == "HR"])
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-3: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nFiltering records where the Name of individuals begins with A or D")
#print (df[df["Name"] == "A*"])
print(df[df['Name'].str.startswith(('Al', 'D'), na=False)])
         
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-4: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nFiltering records where the Name of individuals begins with A or D or Ends with b")
#print (df[df["Name"] == "A*"])
print(df[df['Name'].str.startswith(('Al', 'D'), na=False) | df['Name'].str.endswith('b', na=False)])
         
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-5: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nFiltering records where the Name of individuals begins with A or D")
#print (df[df["Name"] == "A*"])
print(df[df['Name'].str.startswith(('Al', 'D'), na=False)])
         
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

