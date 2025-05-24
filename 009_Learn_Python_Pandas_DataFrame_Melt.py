"""
                    Melt 
Convert wide-format data to long format using melt().
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
df1 = pd.melt(df)
print(f"The Wide format of Data Frame is: \n{df1}")