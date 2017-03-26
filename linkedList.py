__author__ = 'siddharth'

import copy

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def display(self):
        current = self
        while current is not None:
            print current.data,
            current = current.next

    def insert(self, data):
            current = self
            while current.next is not None:
                current = current.next
            current.next = Node(data)

    def reverse(self):
        current = copy.deepcopy(self)
        prev = None
        while current.next is not None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.data = current.data
        self.next = prev

N = int(raw_input("Enter Number of elements: "))

head = Node(int(raw_input("Enter Elements: ")))



if __name__ == "__main__":
    for i in range(1,N):
        head.insert(int(raw_input()))
    head.display()
    head.reverse()
    head.display()





