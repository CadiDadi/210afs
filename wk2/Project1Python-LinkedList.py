#########################################

# In this project, you will practice your knowledge of the data structure concept of linked list and nodes by storing a series of string values in a doubly linked list.  You will then retrieve data, modify data values, and print the sequence.

# Getting Started
#     1. Download the file "doubly-linked.py  download" that contains code for a doubly linked list class into your Week 2 folder.
#     2. Complete the missing code for the following functions:
#         addFirst
#         addLast
#         addAtIndex
#         indexOf
#     3. Print the list with print(words)
#     4. Store the items in the list below in the order they are listed and then print the list
#         May
#         the
#         Force
#         be
#         with
#         you
#         !
#     5. Return the index position of "with" in the list and print this value
#     6. Change "you" into "us" on the list
#     7. Add "all" before "!" on the list
#     8. Print the list.

# Expected Output:

#     May the Force be with you !
#     4
#     May the Force be with us all !

#########################################

class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0
    def iter(self):
        # Iterate through the list.
        current = self.head
        while current:
            val = current.data
            current = current.next
            yield val
    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count
    def addFirst(self, data) -> None:
        # Add a node at the front of the list
        node = Node(data)
        node.next = self.head
        self.head = node
        if not self.tail:
            self.tail = node        
        self.count += 1
    def addLast(self, data) -> None:
        # Add a node at the end of the list
        node = Node(data)
        self.count += 1
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)
    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        if index > self.count:
            return
        if (index == self.count):
            self.addLast(data)
            return
        if index == 0:
            self.addFirst(data)
            return
        curr = self.head
        prev = self.head
        for n in range(index):
            prev = curr
            curr = curr.next
        node = Node(data)
        prev.next = node
        node.prev = prev
        node.next = curr
        curr.prev = node
        self.count += 1       
        return
    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0
    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.
        if (index > (self.count-1)):
            return            
        curr = self.head
        prev = self.head
        for n in range(index):
            prev = curr
            curr = curr.next
        prev.next = curr.next
        curr.prev = prev
        self.count -= 1
        if (curr == self.head):
            self.head = curr.next
            curr.prev = None
        elif (curr == self.tail):
            prev.next = None
            self.tail = prev       
        return
    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        current = self.head
        prev = self.head
        while current:
            if current.data == data:
                if current == self.tail:
                    prev.next = None
                    self.tail = prev
                elif current == self.head:
                    current.next.prev = None
                    self.head = current.next
                else:
                    prev.next = current.next
                    current.next = prev
                self.count -= 1
                return
            prev = current
            current = current.next
    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1        
        pos = -1
        for node in self.iter():
            pos += 1
            if data == node:
                return pos
        return pos  
    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        return current.data
    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        current = self.head
        for n in range(index):
            current = current.next
        current.data = value
    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

words = DoublyLinkedList()
words.add('May')
words.add('the')
words.add('Force')
words.add('be')
words.add('with')
words.add('you')
words.add('!')

print(words)
print(words.indexOf("with"))
words[words.indexOf("you")] = "us"
words.addAtIndex("all",words.indexOf("!"))
print(words)








