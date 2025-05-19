"""
NumPy structured arrays are a powerful feature that allow you to create arrays 
with named fields, similar to columns in a table or attributes in a struct. 
They are useful when you want to store heterogeneous data types in a single 
array, making NumPy function like a lightweight database.

Why use Structured Arrays?
•	Efficient storage of heterogeneous data types
•	Easy field-based access
•	Supports sorting and filtering based on specific fields

"""
import numpy as np

print ("""
#######################################################################################################
       Example-1: Creating and Accessing a Structured Array
#######################################################################################################       
""")
# Creating a students_details by dtype
student_dtype = np.dtype([
   ('name', 'U20'), # Unicode with string with max length of 20 characters
   ('age', 'i4'), # 4-byte integer
   ('grade', 'f4') # 4-byte float
])

# Creating a record for the student_details
students = np.array([
    ('Mark', 15, 89.5),
    ('Luke', 18, 98.5),
    ('John', 15, 99.0)
], dtype=student_dtype)

print (f"Student Details are: {students}")
print (f"Grade of John is : {students[students['name'] == 'John']['grade']}")
print (f"List all the names of students in Students table: {students['name']}")
print(f"List all the students names with their ages: {students["name"]}{students["age"]}")
name = students["name"]
age = students["age"]
a = list(zip(name,age))
print (f"Name and grades of students are: {a}")
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")

B = np.array([[10], [20]])  # Shape (2,1)
C = np.array([1, 2, 3] )     # Shape (1,3)
result = B + C  # Broadcasting applied
print(result)

print("$$$$$$$$$$$$$$$$$$$$$$$$$")

A = np.array([
[1,2,3],
[4,5,6],
[7,8,9]
])

# Define a 1D Array (1x3)
B = np.array([10,200,300])
# Perform element-wise addition
result = A + B
print (result)

