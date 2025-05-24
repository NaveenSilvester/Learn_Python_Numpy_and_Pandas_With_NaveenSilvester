"""
Pivot Table
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


print ("""
#######################################################################################################
       Example-1: Pivot Table
#######################################################################################################       
""")
# Pivot table: Average Salary by Department and Name
print("Original Table")
print(df)
# Fill missing Age with the mean
df['Age'] = df['Age'].fillna(df['Age'].mean())

print("After filling missing Age with mean:")
print(df)
# Fill missing Name with 'Unknown'
df['Name'] = df['Name'].fillna('Unknown')
print("\nAfter filling missing Name with 'Unknown'")
print(df)
df['Salary'] = df['Salary'].fillna(df['Salary'].interpolate())
print("After filling missing Age with mean and Salary with interpolate:")

print(df)
pivot_table = df.pivot_table(values='Salary', index='Department', columns='Name', aggfunc='mean')
print("\nPivot Table: Distribution of Salary in each department")
print(pivot_table)

pivot_table = df.pivot_table(values='Age', index='Department', columns='Name', aggfunc='mean')
print("\nPivot Table: Distribution of Age across Departments")
print(pivot_table)

