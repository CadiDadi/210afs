##################################################################
# Instructions:

    # 1 Download the file recursion.py into your Week 2 folder (pasted here):
        # def loop1():
        # # Sum the odd numbers between 1 and 20
        # odd_sum = 0
        # for i in range(20):
        #     if (i % 2) == 1:
        #         odd_sum += i
        # return odd_sum
        # def loop2():
        #     # Sum the even numbers between 1 and 20
        #     i = 0
        #     even_sum = 0
        #     while i < 20:
        #         if (i % 2) == 0:
        #             even_sum += i
        #         i += 1
        #     return even_sum
        # def loop1Rec(num,odd_sum):
        #     # Duplicate the loop1 function using recursion
        # def loop2Rec(num,even_sum):
                # Duplicate the loop2 function using recursion

    # 2 Write the code for loop1Rec so that it produces the same output as the function loop1 , but uses recursion instead.

    # 3 Write the code for loop2Rec so that it produces the same output as the function loop2 , but uses recursion instead

    # 4 Call each of the four functions and print the results for each.

# Expected Output:
    # Sum of odds between 1 and 20 using 'for' loop =  100
    # Sum of odds between 1 and 20 using recursion =  100
    # Sum of evens between 1 and 20 using 'while' loop =  90
    # Sum of evens between 1 and 20 using recursion =  90
##################################################################

def loop1():
    # Sum the odd numbers between 1 and 20
    odd_sum = 0
    for i in range(20):
        if (i % 2) == 1:
            odd_sum += i
    return odd_sum

def loop2():
    # Sum the even numbers between 1 and 20
    i = 0
    even_sum = 0
    while i < 20:
        if (i % 2) == 0:
            even_sum += i
        i += 1
    return even_sum

# Write the code for loop1Rec so that it produces the same output as the function loop1 , but uses recursion instead.
def loop1Rec(num,odd_sum):
    if (num >= 20):
        return odd_sum
    elif (num % 2) == 1:
        odd_sum += num   
    return loop1Rec(num+1,odd_sum)

# Write the code for loop2Rec so that it produces the same output as the function loop2 , but uses recursion instead
def loop2Rec(num,even_sum):
    if (num >= 20):
        return even_sum
    elif (num % 2) == 0:
        even_sum += num
    return loop2Rec(num+1,even_sum)


print("Sum of odds between 1 and 20 using 'for' loop = ",loop1())
results = 0
print("\n")
print("Sum of odds between 1 and 20 using recursion = ", loop1Rec(0,results))
print("\n")
print("Sum of evens between 1 and 20 using 'while' loop = ",loop2())
results = 0
print("\n")
print("Sum of evens between 1 and 20 using recursion = ", loop2Rec(0,results))



