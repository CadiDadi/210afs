# Getting Started

# 1 Download the file hashing.py file into your Week 4 folder.
# 2 Write the missing code in the HashTable class for the following methods:
# - hashfunction
# - rehash
# - put
# - get
# 3 Create a hash table with a size of 10.
# 4 The primary hash function will use key modulus table_size
# 5 Resolve collisions using double hashing where the secondary hash function is key div table_size where div is integer division (//)  * Note that the double hashing algorithm used is not perfect and there may be unresolved collisions where data is lost.  
# 6 Store the items in the table below
# 7 Print the slots
# 8 Print the data
# 9 Print the value of the data for key 52
# 10 Challenge: Create a new secondary hash function using your own algorithm that avoids all collisions with this data set.
# 11 Challenge: Print the updated slots
# 12 Challenge: Print the updated data

# Input:

# Key	Data
# 69	A
# 66	B
# 80	C
# 35	D
# 18	E
# 52	F
# 89	G
# 70	H
# 12	I

# Expected Output:
 
# [80, 12, 52, None, None, 35, 66, 70, 18, 69]        
# ['C', 'I', 'F', None, None, 'D', 'B', 'H', 'E', 'A']
# F

### hashing.py file code ##########################

class HashTable:
    def __init__(self) -> None:
        self.size = 10
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def hashfunction(self,key):
        # Insert your hashing function code
        return key % self.size

    def rehash(self,key):
        # Insert your secondary hashing function code
        return key // self.size

    def put(self,key,data):
        # Insert your code here to store key and data 
        h1 = self.hashFunction(key, self.size)
        if self.slots[h1] == None:
            self.slots[h1] = key
            self.slots[h1] = data
            else:
                if self.slots ==

        # else:
        #   print("collision")

    def get(self,key):
        # Insert your code here to get data by key

    def __getitem__ (self,key):
        return self.get(key)

    def __setitem__ (self,key,data):
        self.put(key,data)


# Store remaining input data
H = HashTable()
H[69] = 'A'
H[66] = 'B'
H[80] = 'C'
H[35] = 'D'
H[18] = 'E'
H[52] = 'F'
H[89] = 'G'
H[70] = 'H'
H[12] = 'I'

# print the slot values
print(H.slots)
# print the data values
print(H.data)
# print the value for key 52
print(H[52])
