
# 1. Create a file called “palindrome.py” in your Week 3 folder.

# 2. Create two classes, stack and queue, that implement the following functions.  Do not use the code in the book, but create your own classes using the data structures covered so far:

# Stack:
class Stack:
    def __init__(self):
        self.items = []
    #  push(e) – Adds the element ‘e’ to the top of the stack
    def push(self, data):
        self.items.append(data)
    #  pop() – Deletes the top most element of the stack and returns its ___?
    def pop(self):
        data = self.items.pop() 
        return data
    #  size() – Returns the size of the stack
    def size(self):
        return len(self.items)
    #  isEmpty() – Returns whether the stack is empty
    def isEmpty(self):
        return self.items == []
    #  peek() – Returns a reference to the top most element of the stack value. Does not remove the element.
    def peek(self):
        return self.items[0]

# Queue:
class Queue:
    def __init__(self):
        self.items = []
    #  enqueue(e) - Adds the element 'e' to the queue. 
    def enqueue(self, data):
        self.items.insert(0, data)
    #  dequeue() - Removes an item from the queue. 
    def dequeue(self):
        data = self.items.pop()
        return data
    #  size() - Returns the size of the queue
    def size(self):
        return len(self.items)
    #  isEmpty() - Returns whether the queue is empty
    def isEmpty(self):
        return self.items == []
    #  peek() - Returns a reference to the front item in the queue. Does not remove the element.
    def peek(self):
        return self.items[0]

# 3. Create a function called "isPalindrome" that accepts a string as a parameter and returns either True or False if the string is a Palindrome. A Palindrome String is a collection of alphabets which remains the exact same way when read backwards.  Note: This function must use both the Stack and Queue class.
def isPalindrome(str):
    strStack = Stack()
    strQueue = Queue()
    for element in str:
        strStack.push(element)
        strQueue.enqueue(element)
# 4. Run your code against the following strings to determine whether they are palindromes or not and print the results.
    results = True
    for i in range(int(len(str)/2)):
        if (strStack.pop() != strQueue.dequeue()):
            results = False
    return results
    
# Input:
    # "racecar"
    # "noon"
    # "python
    # "madam"
print(isPalindrome("racecar"))
print(isPalindrome("noon"))
print(isPalindrome("python"))
print(isPalindrome("madam"))
# Expected Output:
    # True
    # True
    # False
    # True
print(isPalindrome("13131"))
print(isPalindrome("234"))



