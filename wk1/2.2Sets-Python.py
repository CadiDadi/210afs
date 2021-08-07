# https://www.tutorialspoint.com/python_data_structure/python_sets.htm

#In a Set, items are unordered, unindexed and do not allow duplicate values.

#Unordered means that the items in a set do not have a defined order.

# We cannot access individual values in a set. 

#This means that items in a Set can appear in a different order every time you use them, and cannot be referenced by an index or key.

#A Set is created by placing a sequence of values separted by a comma inside curly brackets {}

progLang = {"python", "c#", "javascript", "java", "c++"}
moreLang = {"rust", "php", "perl", "ruby", "go", "java", "python"}
myNumbers = {1,2,3,4,5}
myFloats = {1.0, 2.1, 3.2, 4.3}

# Add item to set
# Sets cannot have two items with the same value, so adding "python" doesnt work, but can add "pythn"
progLang.add("python")
progLang.add("pythn")
print (progLang)

# find the common values between sets
print(progLang.intersection(moreLang))

# remove last item in a set
removedItem = progLang.pop()
print(progLang)
print(removedItem)

# remove specific item
progLang.discard("c#")
print(progLang)