

#Dictionaries are used to store data in key:value pairs where the keys must be unique.

#A dictionary is a collection which is ordered, as of Python version 3.7, changeable (mutable) and does not allow duplicate key values.

#Storing a value using a key that is already in use, results in the old value being replaced with the new value.

#A Dictionary is created by placing a sequence of keys:values pairs, separted by a comma, inside curly brackets {}

#If you are familiar with Javascript, the notation of key:value pairs should be familiar to you as they are similar to JSON data format.

worldCapitals = {
	"Afghanistan" : "Kabul",
	"Bangladesh" : "Dhaka",
	"Canada" : "Ottawa",
	"Cuba" : "Havana",
	"France" : "Paris",
	"Germany" : "Berlin",
	"Philippines" : "Manila",
	"United Kingdom" : "London",
	"United States" : "Washington D.C."
}

print("\n")
print(worldCapitals)
print("\n")
print(worldCapitals.get("France"))
print("\n")
print(worldCapitals.keys())
print("\n")
print(worldCapitals.items())
print("\n")
keys = worldCapitals.keys()
for key in keys:
    print('"%s" : "%s"' % (key, worldCapitals.get(key)),end=",")
print("\n")
for country, capital in worldCapitals.items():
	print(country + " = " + capital)
print("\n")
worldCapitals.pop("Germany")
print(worldCapitals)
print("\n")
worldCapitals.update({"United States" : "New York"})
print(worldCapitals)
print("\n")
print(worldCapitals.setdefault("Canada"))
print("\n")

print("\n")


















