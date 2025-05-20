"""
Pandas Data Structure
Pandas provides two primary data structures that make data manipulation and analysis efficient.
    1. Series (1-Dimensional Data)
        A Series is a one-dimensional labelled array capable of holding any data type (integers, strings,
        floats, python objects, etc.,)
    
    2. DataFrame (2-Dimensional Data)
        A DataFrame is a 2D Table (like an Excel sheet or a SQL table) with rows and columns

"""
import pandas as pd

print ("""
#######################################################################################################
       Example-1: Creating a Pandas DataFrame
#######################################################################################################       
""")
df = pd.DataFrame({
    "name" : ["Allen", "Kane", "Lambart"],
    "lang" : ["Hindi", "French", "Manadrin"],
    "city" : ["Bangalore", "Colombo", "Beijing"]
})
print(f"DataFrame df contains:\n{df}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-2: Creating a Custom index DataFrame
#######################################################################################################       
""")
data = pd.DataFrame({
    "name" : ["Allen", "Kane", "Lambart"],
    "lang" : ["Hindi", "French", "Mandarin"],
    "city" : ["Bangalore", "Colombo", "Beijing"]
})
print(f"DataFrame df contains:\n{data}")
data.index = ["R1","R2","R3"]
print(f"DataFrame with Custome index looks like:\n{data}")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-2: Accessing a column
#######################################################################################################       
""")
data = pd.DataFrame({
    "name" : ["Allen", "Kane", "Lambart"],
    "lang" : ["Hindi", "French", "Mandarin"],
    "city" : ["Bangalore", "Colombo", "Beijing"]
})
print(f"DataFrame df contains:\n{data}")
data.index = ["R1","R2","R3"]
print(f"DataFrame with Custom index looks like:\n{data}")
print(f"Fetching the names:\n{data["name"]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-3: Accessing multiple column
       Note: For Multiple columns the query has two [[]]
#######################################################################################################       
""")
data = pd.DataFrame({
    "name" : ["Allen", "Kane", "Lambart"],
    "lang" : ["Hindi", "French", "Mandarin"],
    "city" : ["Bangalore", "Colombo", "Beijing"]
})
print(f"DataFrame df contains:\n{data}")
data.index = ["R1","R2","R3"]
print(f"DataFrame with Custom index looks like:\n{data}")
print(f"Fetching the names and city:\n{data[["name", "city"]]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-4: Accessing by Rows with its labels
        df.loc[]
#######################################################################################################       
""")
data = pd.DataFrame({
    "name" : ["Allen", "Kane", "Lambart"],
    "lang" : ["Hindi", "French", "Mandarin"],
    "city" : ["Bangalore", "Colombo", "Beijing"]
})
print(f"DataFrame df contains:\n{data}")
data.index = ["R1","R2","R3"]
print(f"DataFrame with Custom index looks like:\n{data}")
print(f"Fetching the Row R1:\n{data.loc["R1"]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")



print ("""
#######################################################################################################
       Example-4: Accessing by Rows with its index
        df.iloc[]
#######################################################################################################       
""")
data = pd.DataFrame({
    "name" : ["Allen", "Kane", "Lambart"],
    "lang" : ["Hindi", "French", "Mandarin"],
    "city" : ["Bangalore", "Colombo", "Beijing"]
})
print(f"DataFrame df contains:\n{data}")
data.index = ["R1","R2","R3"]
print(f"DataFrame with Custom index looks like:\n{data}")
print(f"Fetching the second Row :\n{data.iloc[1]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")