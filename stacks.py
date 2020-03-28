"""Contains code for StackADTs
CPE202
Project 1

Author:
    Eeshan Mishra
"""
from node import *

class StackArray:
    """Stack using resizing array
    Attributes:
        arr (list) : An array
        num_items (int) : number of items
        capacity (int) : capacity
    """

    def __init__(self):

        self.capacity = 2
        self.arr = [None] * self.capacity
        self.num_items = 0

    def __repr__(self):
        """Write signature and purpose
        """
        pass

    def __eq__(self, other):
        """Write signature and purpose
        """
        pass

    def enlarge(self):
        """Write signature and purpose
        """
        self.capacity *= 2
        self.new_arr = [None]*self.capacity
        for item in self.arr:
            self.new_arr.append(item)
        return self.new_arr


    def shrink(self):
        """Write signature and purpose
        """
        self.capacity = self.capacity//2
        self.new_arr = [None] * self.capacity
        for item in self.arr:
            self.new_arr.append(item)
        return self.new_arr

    def is_full(self):
        """Returns False unless stack is full
        Must have O(1) performance"""
        return self.size() == self.capacity


    def is_empty(self):
        """Returns False unless stack is empty
        Must have O(1) performance"""
        return self.size() == 0

    def push(self, item):
        """pushes the item on top of the stack; if the stack is full, raises an IndexError
        Must have O(1) performance"""

        if self.is_full():
            self.arr = self.enlarge()
        self.num_items += 1
        if 4 <= self.capacity/self.num_items:
            self.arr = self.shrink()
        self.arr[self.num_items - 1] = item

    def pop(self):
        """Removes the item on the top of the stack
        """
        if 4 <= self.capacity/self.num_items:
            self.arr = self.shrink()
        self.num_items -= 1
        return self.arr[self.num_items]

    def peek(self):
        """Returns the item on top of the stack
        """
        if self.is_empty():
            raise IndexError
        return self.arr[0]

    def size(self):
        """Returns the size of the array
        """
        return self.num_items


class StackLinked:
    """Stack using linked list
    Attributes:
        top (int) : pointer to the top of the stack
        num_items (int) : number of items
    """

    def __init__(self):
        """Write signature and purpose
        """
        self.top = None
        self.num_items = 0

    def is_empty(self):
        """Returns True if the linked list is empty else False
        """
        return self.num_items == 0

    def push(self, item):
        """Pushes an item onto the top of the stack
        """
        node = Node(item)
        node.next = self.top
        self.top = node
        self.num_items += 1

    def pop(self):
        """Pops item from the stack unless its empty
        """
        if self.size() == 0:
            raise IndexError

    def peek(self):
        """returns the next item to be popped off the top of the stack
        """
        if self.size() == 0:
            raise IndexError
        return self.top.data

    def size(self):
        """returns the size of the linked list
        """
        return self.num_items

