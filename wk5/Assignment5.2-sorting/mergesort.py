# Getting Started
    # In your Week 5 folder, create a folder called ‘sorting’ for this assignment.
    # Download the mergesort.py
    # Complete the code for the mergeSort function to sort a list of elements using the merge sort algorithm.
    # At each stage, print the status of the list as it is split and merged.
    # Print the final list of elements in sorted order.
 
# Sample Input:
# [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]

# Expected Output:
# Splitting  [55, 31, 26, 20, 63, 7, 51, 74, 81, 40]
# Splitting  [55, 31, 26, 20, 63]
# Splitting  [55, 31]
# Splitting  [55]
# Merging  [55]
# Splitting  [31]
# Merging  [31]
# Merging  [31, 55]
# …….
# Merging  [40]
# Merging  [40, 81]
# Merging  [40, 74, 81]
# Merging  [7, 40, 51, 74, 81]
# Merging  [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

# Sorted: [7, 20, 26, 31, 40, 51, 55, 63, 74, 81]

#################################

def mergeSort(nlist):
    print("Splitting ",nlist)
    # insert your code to complete the mergeSort function
    if len(nlist)>1:
        mid = len(nlist)//2
        lefthalf = nlist[:mid]
        righthalf = nlist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        nlist = merge(nlist,lefthalf,righthalf)
    print("Merging ",nlist)

def merge(nlist,lefthalf,righthalf):
    i=j=k=0       
    while i < len(lefthalf) and j < len(righthalf):
        if lefthalf[i] < righthalf[j]:
            nlist[k]=lefthalf[i]
            i=i+1
        else:
            nlist[k]=righthalf[j]
            j=j+1
        k=k+1

    while i < len(lefthalf):
        nlist[k]=lefthalf[i]
        i=i+1
        k=k+1

    while j < len(righthalf):
        nlist[k]=righthalf[j]
        j=j+1
        k=k+1
    return nlist

mergeList = [ 55 ,  31 ,  26 ,  20 ,  63 ,  7 ,  51 ,  74 ,  81 ,  40 ]
mergeSort(mergeList)
print("Sorted mergeList:",mergeList)