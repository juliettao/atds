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
    


class Queue(object):
    """Describes a queue that can be used with enqueue
    and dequeue methods.
    """
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)
    
    def size(self):
        return len(self.queue)
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def __repr__(self):
        return str(self.queue)
    
class Deque():
    def __init__(self):
        self.deque = []

    def add_front(self, item):
        self.deque.insert(0, item)

    def add_rear(self, item):
        self.deque.append(item)

    def remove_front(self):
        return self.deque.pop(0)
    
    def remove_rear(self):
        return self.deque.pop()
    
    def size(self):
        return len(self.deque)
    
    def is_empty(self):
        return len(self.deque) == 0
            

class Node(object):
    """Defines a node in the object class to be used in unordered lists
    """
    def __init__(self, data):
        self.data = data
        self.next = None
    def set_data(self, data):
        self.data = data
    def get_data(self):
        return self.data
    def set_next(self, next):
        self.next = next
    def get_next(self):
        return self.next
    def __repr__(self):
        return "[data=" + str(self.data) + "[next=" + str(self.next) + "]"
    
class UnorderedList():
    """Maintains an unordered list via a linked series of Nodes
    """
    def __init__(self):
        self.head = None

    def add(self, new_data):
        """Creates a new Node based on the data, and adds it to the 
        beginning of the list.
        """
        temp_node = Node(new_data)
        temp_node.set_next(self.head)
        self.head = temp_node

    def remove(self, data):
        """Removes multiple occurrences of data on the list, 
        which requires going through the entire list until
        you hit the end, or nothing if the data isn't on the list.
        """
        current = self.head
        previous = None
        while current != None and self.head != None:    # Have to search entire list
            if current.get_data() == data:              # need to remove it
                if previous == None:                    # we're at the head
                    self.head = current.get_next()
                    current = current.get_next()
                else:
                    previous.set_next(current.get_next())
                    current = current.get_next()
            else:                                       # pass on through
                previous = current
                current = current.get_next()
        
    def pop(self):
        """Removes the item at the top of the stack and
        returns it.
        """
        return self.ul.pop(0)

    def length(self):
        """Traverses the entire length of the UnorderedList to identify 
        how many values (nodes) there are in the list.
        """
        node_count = 0                  # local variable for counting
        current = self.head             # start at the beginning
        while current != None:          # if we're not at the end of the list
            current = current.get_next()     # move to the next node
            node_count += 1                 # increment node counter
        return node_count
    
    def search(self, data):
        """Returns True if the data is on the list
        """
        current = self.head
        while current != None:
            if current.get_data() == data:
                return True
            else:
                current = current.get_next()
        return False
    
    def is_empty(self):
        return self.head == None

    def append(self, data):
        """Appends an item to the end of the list
        """
        temp = Node(data) 
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        current.set_next(temp)

    def index(self, data):
        """Returns the index of the first occurence of the data
        in the list.
        """
        if self.head == None:
            return None
        current = self.head
        index = 0
        while current != None and current.get_data() != data:
            current = current.get_next()
            index += 1
        if current == None:
            return None
        else:
            return index

    def insert(self, position, data):
        """Inserts the piece of data at the indicated position.
        """
        temp = Node(data)
        index = 0
        current = self.head
        previous = None
        while index < position:
            previous = current
            current = current.get_next()
            index += 1
        if index == 0:
            temp.set_next(current)
            self.head = temp
        else:
            previous.set_next(temp)
            temp.set_next(current)
            
    def pop(self, index=-1):
        """Removes item at position index, or at the end of the list
        (-1) if no index is indicated.
        From Mr. White's atds file
        """
        if self.head == None:
            return None      # Can't pop from empty list
        if index == -1:
            current = self.head
            previous = None
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            result = current.get_data()
            previous.set_next(None)
            return result
        elif index == 0:
            current = self.head
            result = current.get_data()
            self.head = current.get_next()
            return result
        else:       # returning from middle of list?
            current = self.head
            previous = None
            position = 0
            while position < index:
                previous = current
                current = current.get_next()
                position += 1
            result = current.get_data()
            previous.set_next(current.get_next())
            return result
        
    def __repr__(self):
        """Creates a representation of the list suitable for printing,
        debugging.
        """
        result = "UnorderedList["
        next_node = self.head
        while next_node != None:
            result += str(next_node.get_data()) + ","
            next_node = next_node.get_next()
        result = result + "]"
        return result
    
class UnorderedListStack(object):
    """Implements a Stack using the UnorderedList class.
    From Mr. White's atds file
    """
    def __init__(self):
        self.ul = UnorderedList()

    def push(self, item):
        """Pushes an item onto the top of the stack"""
        self.ul.add(item)

    def pop(self):
        """Removes the item at the top of the stack and
        returns it.
        """
        return self.ul.pop(0)
    
    def peek(self):
        """Examines the item at the top of the stack
        and returns that value. Awkward: we don't have
        a way to look at data at the beginning of an
        Unordered List!"""
        value = self.ul.pop(0)
        self.ul.add(value)
        return value

    def size(self):
        return self.ul.length()

    def is_empty(self):
        return self.ul.is_empty()
    
    def __repr__(self):
        return str(self.ul)
    

class HashTable(object):
    """Describes a hash table based on two lists, slots, and values,
    and describes putting and getting values onto that table.
    Hash function is the mod % function, and collisions are handled 
    using linear probing.
    """
    def __init__(self, size):
        """Create empty list for the Map
        """
        self.keys = [None] * size
        self.data = [None] * size
        self.size = size

    def __repr__(self):
        return "Keys:   " + str(self.keys) + "\n" + "Values: " + str(self.data)

    def hash_function(self, key):
        return key % self.size

    def put(self, key, value):
        hash_value = key % self.size
        while self.keys[hash_value] != None and self.keys[hash_value] != key:
            hash_value += 1
        if self.keys[hash_value] == key:
            self.data[hash_value] = value
        else:
            self.keys[hash_value] = key
            self.data[hash_value] = value


    def get(self, key):
        hash_value = key % self.size
        while self.keys[hash_value] != None and self.keys[hash_value] !=key:
            hash_value += 1
        if self.keys[hash_value] == key:
            return self.data[hash_value]
        else:
            return None
        
    def rehash(self, old_hash):
        return (old_hash + 1) % self.size
    
class BinaryTree(object):
    def binary_tree(r):
        """Constructs a binary tree with value r
        and no children.
        """
        return [r, [], []]

    def get_root_val(root):
        return root[0]
        
    def set_root_val(root, new_val):
        root[0] = new_val
        
    def get_left_child(root):
        return root[1]
        
    def get_right_child(root):
        return root[2]
    
    def insert_left(root, value):
        """Insert a new subtree of "value" as a left child.
        """
        new_subtree = BinaryTree(value)    # create new node
        new_subtree[1] = root[1]            # set current left_child to 
                                            # left_child of new node
        root[1] = new_subtree               # set root left_child reference
                                            # to this new subtree

    def insert_right(root, value):
        """Insert a new subtree of "value" as a right child.
        """
        new_subtree = BinaryTree(value)    # create new node
        new_subtree[2] = root[2]            # set current right_child to 
                                            # left_child of new node
        root[2] = new_subtree               # set root right_child reference
                                        # to this new subtree

def main():
    pass

if __name__ =="__main__":
    main ( )

