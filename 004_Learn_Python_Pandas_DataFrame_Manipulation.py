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
       Example-2: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nFiltering records where the Name of individuals begins with A or D")
#print (df[df["Name"] == "A*"])
print(df[df['Name'].str.startswith(('Al', 'D'), na=False)])
         
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-3: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nFiltering records where the Name of individuals begins with A or D or Ends with b")
#print (df[df["Name"] == "A*"])
print(df[df['Name'].str.startswith(('Al', 'D'), na=False) | df['Name'].str.endswith('b', na=False)])
         
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-2: Filtering Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nFiltering records where the Name of individuals begins with A or D")
#print (df[df["Name"] == "A*"])
print(df[df['Name'].str.startswith(('Al', 'D'), na=False)])
         
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-4: Sorting Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
print(f"\nSorting the DataFrame with descending order of their salary")
print(f"{df.sort_values("Salary", ascending=False)}")        
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-5: Grouping and Aggregating Data
#######################################################################################################       
""")
print(f"Original DataFrame: \n{df}")
grouped = df.groupby('Department')['Salary'].mean().reset_index()
print("\nAverage Salary by Department:")
print(grouped)
print("\nCount by Department:")
grouped = df.groupby('Department').count().reset_index()
print(grouped)    
print("\nCount by Department, Salary and Age:")  
grouped = df.groupby('Department')[["Salary","Age"]].mean().reset_index()
print(grouped)   
df.groupby('Department')

# Count of non-null Names by Department
grouped_c = df.groupby('Department')['Name'].count().reset_index()
print("\nCount of Names by Department:")
print(grouped_c)

# **Merge the count column properly**
grouped_mean = grouped.merge(grouped_c, on="Department", how="left")
grouped_mean.rename(columns={"Name": "counts"}, inplace=True)

print("\nFinal DataFrame with Counts:")
print(grouped_mean)

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-6: Merging and Joining
       Use merge() or concat() to combine DataFrames.
#######################################################################################################       
""")

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', None],
    'Age': [25, np.nan, 30, 22, 28],
    'Salary': [50000, 60000, np.nan, 45000, 52000],
    'Department': ['HR', 'IT', 'IT', 'Marketing', 'HR']
}
df = pd.DataFrame(data)

data2 = {
    'Department': ['HR', 'IT', 'Marketing'],
    'Location': ['New York', 'San Francisco', 'Chicago']
}
df2 = pd.DataFrame(data2)
print(f"\nDataFrame-1 is :\n{df}")
print(f"\nDataFrame-2 is :\n{df2}")

# Merge DataFrames on Department
merged_df = pd.merge(df, df2, on='Department', how='left')
print("\nMerged DataFrame (Merged based on Department):")
print(merged_df)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
