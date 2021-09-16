# In your Week 5 folder, create a folder called ‘searching’ for this assignment.
# Create a binarysearch.py file
# Write the code to perform a binary search on a sorted list.  The function should accept a sorted list and the value to search for as inputs.
# The function should return either True or False depending if the provided value was found in the sorted list.

# Sample Input:

# [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] find 31
# [7, 20, 26, 31, 40, 51, 55, 63, 74, 81] find 77
# ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"] find "Delta"

# Expected Output:

# True
# False
# True

list1 = [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]
list2 = ["Alpha", "Beta", "Delta", "Epsilon", "Gamma", "Theta", "Zeta"]

def binary_search(item_list, item):
	first = 0
	last = len(item_list) - 1
	found = False
	while first <= last and not found:
		mid = (first + last) // 2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found
	
print(binary_search(list1, 31))
print(binary_search(list1, 77))
print(binary_search(list2, "Delta"))