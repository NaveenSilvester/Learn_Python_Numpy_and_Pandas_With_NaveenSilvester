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
       Example-1: Creating a Series
#######################################################################################################       
""")
s1 = pd.Series([10,20,30,40,50])
print (f"Series S1 of Pandas Looks like this:\n{s1}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

print ("""
#######################################################################################################
       Example-2: Accessing Elemetnts of a Series
#######################################################################################################       
""")
s1 = pd.Series([10,20,30,40,50])
print (f"Series S1 of Pandas Looks like this:\n{s1}")
print (f"First Element of s1 is: {s1[0]}")
print (f"Accessing 1:3 element from series s1: \n{s1[0:3]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-3: Creating a Custom Index for a Series
#######################################################################################################       
""")
s1 = pd.Series([10,20,30,40,50], index=["A", "B", "C", "D", "E"])
print (f"Series S1 of Pandas Looks like this:\n{s1}")
print (f"First Element of s1 is: {s1[0]}")
print (f"Accessing 1:3 element from series s1: \n{s1[0:3]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")


print ("""
#######################################################################################################
       Example-4: Accessing a Series by Index Label
#######################################################################################################       
""")
s1 = pd.Series([10,20,30,40,50], index=["A", "B", "C", "D", "E"])
print (f"Series S1 of Pandas Looks like this:\n{s1}")
print (f"Value of Element in the row A s1 is: {s1["A"]}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")