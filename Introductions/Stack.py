"""
A stack is a data structure whose primary purpose is to store and
return elements in Last In First Out order.
1. Implement the Stack class using an array as the underlying storage structure.
    Make sure the Stack test pass.
2. Re-implement the Stack class, this time using the linked list implementation
    as the underlying storage structure.
    Make sure the Stack tests pass.
3. What is the difference between using an array vs. a linked list when
    implementing a Stack?

"""


class Stack:
    def __init__(self):
        self.size = 0
        self.storage = []

    def __len__(self):
        return self.size

    def push(self, value):
        # add an element to the front of the array
        self.size += 1
        self.storage.insert(0, value)

    def pop(self):
        # check if empty
        if len(self.storage) == 0:
            return None
        # remove the first element in storage
        self.size -= 1
        node = self.storage.pop(0)
        return node


new_stack = Stack()
print(len(new_stack))
new_stack.push(2)
new_stack.push(3)
new_stack.push(5)
print(len(new_stack))
print(new_stack.storage)
new_stack.pop