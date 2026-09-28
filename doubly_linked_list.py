"""
Title: Doubly Linked List
Description: Implement the primitive operations of a doubly linked list
"""

# This defines the node class.
class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next

# This defines the doubly linked list class.
class DoublyLinkedList:
    def __init__(self):
        self.first = None #Reference to the head of the list.
        self.last = None  #Reference to the tail of the list.
        self.length = 0   #Keeps track of the length of the list.

    def IsEmptyList(self):
        return self.length == 0

    #This function adds a new node to the head of the list.
    def Prepend(self, value):
        self.first = Node(value, None, self.first)
        if self.IsEmptyList():
            self.last = self.first
        else:
            self.first.next.prev = self.first
        self.length += 1 

    #This function adds a new node to the tail of the list.
    def Append(self, value):
        self.last = Node(value, self.last, None)
        if self.IsEmptyList():
            self.first = self.last
        else:
            self.last.prev.next = self.last
        self.length += 1

    #This function removes the first element at the head of the list.
    def RemoveFirst(self):
        if self.IsEmptyList():
            return "There are no elements to remove!"
        x = self.first.value
        self.first = self.first.next
        if self.length == 1:
            self.last = self.first
        else:
            self.first.prev = None
        self.length -= 1
        return x

    #This function removes the last element at the tail of the list.
    def RemoveLast(self):
        if self.IsEmptyList():
            return "There are no elements to remove!"
        x = self.last.value
        self.last = self.last.prev
        if self.length == 1:
            self.first = self.last
        else:
            self.last.next = None
        self.length -= 1
        return x

    #This function adds a new node after the first occurence of a value in the list.
    def InsertAfterAny(self, key, value):
        curr = self.first
        while curr != None and curr.value != key:
            curr = curr.next

        if curr == None:
            return "Target value was not found!"

        curr.next = Node(value, curr, curr.next)
        if curr == self.last:
            self.last = curr.next
        else:
            curr.next.next.prev = curr.next

        self.length += 1

    #This deletes the first node whose value matches the key.
    def DeleteAny(self, key):
        if self.IsEmptyList():
            return "There are no elements to remove!"
        
        curr = self.first
        while curr != None and curr.value != key:
            curr = curr.next

        if curr == None:
            return "Target value was not found!"

        if self.length == 1:
            self.first = self.last = None
        else:
            if curr == self.first:
                self.first = curr.next
            else:
                curr.prev.next = curr.next
            
            if curr == self.last:
                self.last = curr.prev
            else:
                curr.next.prev = curr.prev
        self.length -= 1 

    #This displays the list starting at its head.
    def DisplayForward(self):
        if self.IsEmptyList():
            return("List is empty!")
            
        curr = self.first
        result = ""
        while curr is not None:
            result += f"{curr.value} ->"
            curr = curr.next
        result = result[:-3]

        return result
    #This displays the list starting at its tail.
    def DisplayBackward(self):
        if self.IsEmptyList():
            return("List is empty!")
            
        curr = self.last
        result = ""
        while curr is not None:
            result += f"{curr.value} ->"
            curr = curr.prev
        result = result[:-3]

        return result



