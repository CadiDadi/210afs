#Tuple items are ordered, unchangeable, and allow duplicate values.

#Tuple items are indexed with the first item having an index of [0], the second item has an index of [1] etc.

#The Tuple is unmutable (ie: unchangeable), meaning that we can not change, add, and remove items in a tuple after it has been created.

#A Tuple may contain multiple different DataTypes include integers, strings, floats, booleans, lists and objects

#Tuples are created by placing a sequence of values separated by a comma inside round brackets ()

progLang = ("python", "c#", "javascript", "java", "c++","python")

myNumbers = (1,2,3,4,5)
myFloats = (1.0, 2.1, 3.2, 4.3)

myMixed = ("Hello", True, 6, ["item1","item2","item3"], 3.14)

print(progLang.count("python"))
print(progLang.index("javascript"))

print(len(progLang))

print(myMixed)
myMixed[3][0] = "A"
print(myMixed)