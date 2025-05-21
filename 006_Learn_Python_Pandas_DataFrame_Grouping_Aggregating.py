print ("""
#######################################################################################################
       Example-1: Grouping and Aggregating Data
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

