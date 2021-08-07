# 1. store the data sets listed below in one of four built-in Python data structures (lists, tuples, sets, dictionaries)
# 2. choose the appropriate data structure for the data provided and for the tasks that must be performed on each data set.  You can only use each data structure once.
# 3. Complete each given task for each of the data sets.

# Given:

# Data1 = 7, False, "Apple", True, 7, 98.6 
# Data2 = "July", 4, 8, "Tango", 4.3, "Bingo"
# Data3 = "A", 7, -1, 3.14, True, 7  
# Data4 =  "name" = "Joe",  "age" = 26,   "active" = True,  "hourly_wage" = 14.75

# Data Structures:

# Tuple ()
Data1 = (7, False, "Apple", True, 7, 98.6) 
# Set {}
Data2 = {"July", 4, 8, "Tango", 4.3, "Bingo"} 
# List []
Data3 = ["A", 7, -1, 3.14, True, 7]  
# Dictionary {}
Data4 = {
	"name" : "Joe", 
	"age" : 26,
	"active" : True,
	"hourly_wage" : 14.75
	} 

# Tasks:

# Data1 - Count the number of items
print(len(Data1))
print("\n")
# Data1 - Find the value of the third item stored in the data set
print(Data1[2])
print("\n")
# Data1 - Count the number of times 7 appears
print(Data1.count(7))
print("\n")
# Data2 - Remove a random element from the data set
Data2.pop()
# Data2 - Add "Alpha" to the data set
Data2.add("Alpha")
# Data2 - Print data set
print(Data2)
print("\n")
# Data3 - Print the data set in reverse order
Data3.reverse()
# Data3 - Change the second value in the data set to ‘B’
Data3[1] = "B"
print(Data3)
print("\n")
# Data3 - Remove the last item and print the data set
Data3.pop()
print(Data3)
print("\n")
# Data4 - Change "active" to False
Data4["active"] = False
# Data4 - Add "address" with a value of "123 West Main Street"
Data4["address"] = "123 West Main Street"
print(Data4)
print("\n")
# Data4 - Print the weekly salary for Joe if he worked a full 40 hour week.
print(Data4["hourly_wage"] * 40)
print("\n")
# Data4 - Print the data set
print(Data4)
print("\n")