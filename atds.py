#!/usr/bin/env python3
"""
atds.py
the module containing all of the data structures used in ATCS at poly.
"""
__author__ = "Juliet Lord" 
__version__ = "2024-02-13"


class Stack(object):
    def __init__(self):
        self.st = []

    def push(self, item):
        self.st.append(item)

    def pop(self):
        if len(self.st) > 0:
            return self.st.pop()
        else:
            return None
    
    def peek(self):
        if len(self.st) > 0:
            return self.st(-1)
        else:
            return None
        
    def size(self):
        return len(self.st)
    
    def is_empty(self):
        return len(self.st) == 0
    


class Queue():
    def __init__(self):
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        return self.q.pop(0)
    
    def peek(self):
        if len(self.q) > 0:
            return self.q[-1]
        else:
            return None
        
    def size(self):
        return len(self.q)
    
    def is_empty(self):
        return len(self.q) == 0
    
    def __repr__(self):
        return str(self.q)
