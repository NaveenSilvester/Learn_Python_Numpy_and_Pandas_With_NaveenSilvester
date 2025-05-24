"""
            Crosstabulation (Crosstab) in Pandas
It is powerful tool for summarizing relationship between categorical variables.
It helps in analyzing patterns and frequency distributions.
"""

print ("""
#######################################################################################################
       Example-1: crosstab()
It is powerful tool for summarizing relationship between categorical variables. It helps in analyzing 
       patterns and frequency distributions.
#######################################################################################################       
""")
import pandas as pd
import numpy as np
data = {
"Gender": ['Male', 'Female', 'Female', 'Male', 'Female', 'Male'],
"Product": ['A', 'B', 'A', 'A', 'C', 'B']
} 
df = pd.DataFrame(data)

print(f"Original Data:\n{df}")
print(f"Let's crete a cross tab of Gender vs Product")
print(f"{pd.crosstab(df['Gender'], df['Product'])}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: crosstab()
It is powerful tool for summarizing relationship between categorical variables. It helps in analyzing 
       patterns and frequency distributions.
#######################################################################################################       
""")
import pandas as pd
import numpy as np
data = {
    'Category': ['Electronics', 'Clothing', 'Electronics', 'Clothing', 'Electronics', 'Clothing'],
    'Region': ['North', 'South', 'North', 'South', 'South', 'North'],
    'Sales': [1000, 500, 1500, 700, 1200, 800]
}
df = pd.DataFrame(data)

print(f"Original Data:\n{df}")
print(f"Let's crete a cross tab of Category vs Regions")
new = pd.crosstab(df['Category'], df['Region'], values=df['Sales'], aggfunc='sum', margins=True)
print(f"{new}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-3: crosstab()
It is powerful tool for summarizing relationship between categorical variables. It helps in analyzing 
       patterns and frequency distributions.
#######################################################################################################       
""")
import pandas as pd
import numpy as np
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Grade': ['A', 'B', 'A', 'C', 'B', 'A']
}
df = pd.DataFrame(data)

print(f"Original Data:\n{df}")
print(f"Let's crete a cross tab of Gender vs Subject, Grade")
crosstab_result = pd.crosstab(df['Gender'], [df['Subject'], df['Grade']],  margins=True)
print(f"{crosstab_result}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-4: crosstab()
It is powerful tool for summarizing relationship between categorical variables. It helps in analyzing 
       patterns and frequency distributions.
#######################################################################################################       
""")
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
    'Gender': ['Female', 'Male', 'Male', 'Male', 'Female', 'Male'],
    'Subject': ['Math', 'Science', 'Math', 'Science', 'Math', 'Science'],
    'Score': [95, 88, 78, 85, 92, 80]
}

df = pd.DataFrame(data)
print(f"Let's crete a cross tab of Gender vs Subject")
crosstab_scores = pd.crosstab(df['Gender'], df['Subject'], values=df['Score'], aggfunc='mean', margins=True)
print(f"{crosstab_scores}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")