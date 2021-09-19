# SCRIMBA EXPLANATION: https://scrimba.com/scrim/cE6e8PTE

# Getting Started:

# In your Week 6 folder, download the file called ‘quick-sort.py’ for this assignment.
# Review the code so that you understand how the "Divide and Conquer" technique works.
# In this code, we utilized the first element of the list to be our pivot point.  This was just for convenience.  There are multiple of different methods for selecting a pivot point.
# Review the section "Deterministic Selection" in chapter 11 of your text book for another possible method.
# Search online for other pivot point methods for Quick Sort algorithm.
# Implement at least three alternatives besides selecting the first element as the pivot point.
# You may want to verify that your sorting code works first on a smaller list of numbers.
# Compare the times necessary to sort a random list of 1,000 elements and display their execution time.
# Did any particular method perform better?  
 

# Sample Output:

# The execution time is: 0.004999876022338867

import time
import random

def quick_sort(a_list, start, end):
    # list size is 1 or less (which doesn't make sense)
    if start >= end:
        return

    # Call the partition helper function to split the list into two section 
    # divided between a pivot point

# Alternatives
    # pivot = partitionStart(a_list, start, end)
    # pivot = partitionSecond(a_list, start, end)
    # pivot = partitionMiddle(a_list, start, end)
    pivot = partitionEnd(a_list, start, end)

    quick_sort(a_list, start, pivot-1)
    quick_sort(a_list, pivot+1, end)
        
def partitionStart(a_list, start, end):
    return partition(a_list, start, end)

def partitionSecond(a_list, start, end):
    if start < end:
        a_list[start], a_list[start+1] = a_list[start+1], a_list[start]
    return partition(a_list, start, end)

def partitionMiddle(a_list, start, end):
    if start < end:
        a_list[start], a_list[(start+end)//2] = a_list[(start+end)//2], a_list[end]
    return partition(a_list, start, end)

def partitionEnd(a_list, start, end):
    if start < end:
        a_list[start], a_list[end] = a_list[end], a_list[start]
    return partition(a_list, start, end)

def partition(a_list, start, end):
    # Select the first element as our pivot point
    pivot = a_list[start]
    
    # Start at the first element past the pivot point
    low = start + 1
    high = end

    while True:
        # If the current value we're looking at is larger than the pivot
        # it's in the right place (right side of pivot) and we can move left,
        # to the next element.
        # We also need to make sure we haven't surpassed the low pointer, since that
        # indicates we have already moved all the elements to their correct side of the pivot
        while low <= high and a_list[high] >= pivot:
            high = high - 1

        # Opposite process of the one above
        while low <= high and a_list[low] <= pivot:
            low = low + 1

        # We either found a value for both high and low that is out of order
        # or low is higher than high, in which case we exit the loop
        if low <= high:
            # Swap the values
            a_list[low], a_list[high] = a_list[high], a_list[low]
            # The loop continues
        else:
            # We exit out of the loop
            break

    # Swap the values
    a_list[start], a_list[high] = a_list[high], a_list[start]

    return high


print("Quick Sort:")
#myList = [54,26,93,17,77,31]
myList = [x for x in range(1000)]
random.shuffle(myList)

#print(myList)
start_time = time.time()
quick_sort(myList,0,len(myList)-1)
end_time = time.time()
#print()
#print("Sorted Listed: ")
#print(myList)   

print(f"The execution time is: {end_time-start_time}")

