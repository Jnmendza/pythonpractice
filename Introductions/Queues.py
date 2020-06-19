# Queue is a line. First in line gets served first. Like a music playlist plays in the order it was built
# FIFO _ first in first out

from linkedList import LinkedList

#class Queue:
#    self.size = 0
#    self.storage = storage_data_structure

# Questions to ask yourself:
#   What's the opposite of FIFO? What data structure exhibit this ordering?
#   What data structures would you use to implement a queue?
#   When is FIFO ordering useful? When is it not?

# Pros and Cons
#   - Queues are simple and intuitive to use and implement
#   - They can be used to serialize data coming in from multiple sources.
#   - Are not general-purpose at all in and of themselves.


class Queue:
    def __int__(self):
        self.size = 0
        self.storage = LinkedList()
        
    def __len__(self):
        return self.size
    
    def enqueue(self, value):
        # Add the new value to the tail of the list
        self.size += 1
        self.storage.add_to_tail(value)
    
    def dequeue(self):
        if self.size == 0:
            return None
        # remove the value from the head of our list
        self.size -= 1
        value = self.storage.remove_head()

        return value
