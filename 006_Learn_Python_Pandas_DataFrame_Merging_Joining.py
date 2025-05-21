
print ("""
#######################################################################################################
       Example-1: Merging and Joining
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

print ("""
#######################################################################################################
       Example-6: Merging and Joining
       Use merge() or concat() to combine DataFrames.
#######################################################################################################       
""")