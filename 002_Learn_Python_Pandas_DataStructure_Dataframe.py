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

print ("""
#######################################################################################################
       Example-5: Creating DataFrame from Dictionary
#######################################################################################################       
""")
data = {
"name": ["Allen", "Kane", "Lambert"],
"section": ["C","D","E"],
"city": ["Bangalore","Columbo","Beijing"]
} 
df = pd.DataFrame(data)
print(f"The newly created DataFrame contains: \n{df}")

df.index = ["R1","R2","R3"]
print(f"DataFrame with Row Headers:\n{df}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-6: Creating DataFrame from List
#######################################################################################################       
""")
list = [
    ["Allen", "C", "Bangalore"],
    ["Kane", "D", "Colombo"],
    ["Lambert", "E", "Beijing"]
]
df = pd.DataFrame(list, columns=["Name", "Section", "City"])

print(f"The newly created DataFrame contains: \n{df}")

df.index = ["L1","L2","L3"]
print(f"DataFrame with Row Headers:\n{df}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-7: Creating DataFrame from List of Dictionaries
#######################################################################################################       
""")
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Paris"},
    {"Name": "Charlie", "Age": 35, "City": "London"}
]
df = pd.DataFrame(data)

print(f"The newly created DataFrame contains: \n{df}")

df.index = ["LD1","LD2","LD3"]
print(f"DataFrame with Row Headers:\n{df}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-8 Creating DataFrame from List of Dictionaries
#######################################################################################################       
""")
data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "Paris"},
    {"Name": "Charlie", "Age": 35, "City": "London"}
]
df = pd.DataFrame(data)

print(f"The newly created DataFrame contains: \n{df}")

df.index = ["LD1","LD2","LD3"]
print(f"DataFrame with Row Headers:\n{df}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-9 Creating DataFrame from CSV files
#######################################################################################################       
""")
data = pd.read_csv("Fruits_comma.csv")
print(data)
print(type(data))
print(data.shape)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-10 Creating DataFrame from NumPy array
#######################################################################################################       
""")
import numpy as np
data = np.array([1,2,3,4,5,6,7,8,9,10])
data = data.reshape(2,5)
print (f"Data is of the data type: {type(data)}")
df = pd.DataFrame(data, columns=["C1","C2","C3","C4","C5"], index=["R1", "R2"])
print (f"The DataFrame looks like this: \n{df}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-11 Creating DataFrame from Excel
#######################################################################################################       
""")
import numpy as np
import pandas as pd
data = pd.read_excel("Nutrition.xlsx", sheet_name="VitaminFruits")
print(f"Data is : \n{data}")
print(f"Data type is: {type(data)}")
print(f"Data shape is: {data.shape}")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-12 Creating DataFrame from JSON
#######################################################################################################       
""")

print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-13 Writing DataFrame to CSV files
#######################################################################################################       
""")
import numpy as np
data = np.array([1,2,3,4,5,6,7,8,9,10])
data = data.reshape(2,5)
print (f"Data is of the data type: {type(data)}")
df = pd.DataFrame(data, columns=["C1","C2","C3","C4","C5"], index=["R1", "R2"])
print (f"The DataFrame looks like this: \n{df}")
df.to_csv("CSV_Output.csv", index=False)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-13 Writing DataFrame to Excel file
#######################################################################################################       
""")
import numpy as np
data = np.array([1,2,3,4,5,6,7,8,9,10])
data = data.reshape(2,5)
print (f"Data is of the data type: {type(data)}")
df = pd.DataFrame(data, columns=["C1","C2","C3","C4","C5"], index=["R1", "R2"])
print (f"The DataFrame looks like this: \n{df}")
df.to_excel("Excel_Output.xlsx", index=False)

with pd.ExcelWriter("Excel_Fromtted_output.xlsx", engine="openpyxl") as writer:
    df.to_excel(writer, sheet_name="MyReport", index=False)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-14 Writing DataFrame to JSON
#######################################################################################################       
""")
import numpy as np
data = np.array([1,2,3,4,5,6,7,8,9,10])
data = data.reshape(2,5)
print (f"Data is of the data type: {type(data)}")
df = pd.DataFrame(data, columns=["C1","C2","C3","C4","C5"], index=["R1", "R2"])
print (f"The DataFrame looks like this: \n{df}")
df.to_json("JSON_Output.json", orient="records", indent=4)
print("Successfully written to JSON file!")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

