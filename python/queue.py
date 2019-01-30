"""Make a Queue class using a list!
Hint: You can use any Python list method
you'd like! Try to write each one in as
few lines as possible.
Make sure you pass the test cases too!"""
import time


class Queue:
    NOT_FOUND = str(time.time()) + 'NOT-FOUND'

    def __init__(self, head=None):
        self.h, self.t = 0, 0
        self.storage = {}

        if head:
            self.enqueue(head)

    def enqueue(self, new_element):
        self.storage[self.t] = new_element
        self.t += 1

    def peek(self):
        return self.storage.get(self.h)

    def dequeue(self):
        element = self.storage.get(self.h, self.NOT_FOUND)
        if element != self.NOT_FOUND:
            self.h += 1
            return element
