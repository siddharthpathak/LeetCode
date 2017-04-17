__author__ = 'siddharth'

import copy

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

        
class linkedList:
    def __init__(self):
        self.head = None

    def insert(self,data):
        temp = Node(data)
        temp.next = self.head
        self.head = temp

    def display(self):
        current = self.head
        while current is not None:
            print current.data
            current = current.next
    def reverse(self):
        current = self.head
        prev = None
        next = None
        while current is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev
       
if __name__ == "__main__":
    linkedlist = linkedList()
    linkedlist.insert(1)
    linkedlist.insert(2)
    linkedlist.insert(3)
    linkedlist.insert(4)
    linkedlist.display()
    linkedlist.reverse()
    linkedlist.display()
