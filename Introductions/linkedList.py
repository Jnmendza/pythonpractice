# class Node:
#    self.value = value
#    self.next = next_node


# class LinkedList:
#   self.head = head_node
#   self.tail = tail_node


# Pros and Cons of LinkedLists
# Unlike arrays, linked lists do not store elements contiguously
#  - Pro: Easier to insert into and delete from the middle of a linked list compared
#        to an array (Why is this the case?)

#  - Con: Linked lists are not as cache-friendly since caches are typically optimized for
#        contiguous memory accesses.

# Linked lists do not need to be allocated with a static amount of memory up-front.
#  - Pro: We can keep adding elements to linked lists as much as we want, unlike arrays with
#        a static amount of allocated memory.


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None  # Stores a node, that is the first node
        self.tail = None  # Stores a node that is the last of the list

    # return all values in the list a --> b --> c --> d --> None
    # How to loop thru the LL
    def __str__(self):
        output = ''
        current_node = self.head # Create a tracker node variable
        while current_node is not None: # loop until its NONE
            output += f'{current_node.value} -> '
            current_node = current_node.next_node # update the tracker node to the next node

        return output

    def add_to_head(self, value):
        # create a new node
        new_node = Node(value)
        # check if list is empty
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # new_node should point to current head
            new_node.next_node = self.head
            # move head to new node
            self.head = new_node

    def add_to_tail(self, value):
        # create a node to add
        new_node = Node(value)
        # check is list is empty
        if self.head and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            # point the node at the current tail, to the new node
            self.tail.next_node = new_node
            self.tail = new_node

    # remove the head and return its value
    def remove_head(self):
        # if list is empty do nothing
        if not self.head:
            return None
        # if list only has one element, set head and tail to None
        if self.head.next_node is None:
            head_value = self.head.value
            self.head = None
            self.tail = None
            return head_value
        # otherwise we have more elements in the list
        head_value = self.head.value
        self.head = self.head.next_node
        return head_value

    def contains(self, value):
        if self.head is None:
            return False

        # Loop through each node, until we see the value, or we cannot go further
        current_node = self.head
        while current_node is not None:
            # check if this is the node we are looking for
            if current_node.value == value:
                return True

            # otherwise, go to the next node
            current_node = current_node.next_node

        return False


linked_list = LinkedList()
# linked_list.add_to_head(0)
# linked_list.add_to_tail(1)
# print(f'does our LL contain 0? {linked_list.contains(0)}')
# print(f'does our LL contain 1? {linked_list.contains(1)}')
# print(f'does our LL contain 2? {linked_list.contains(2)}')
#
# linked_list.add_to_head(2)
# print(f'the start of the list is {linked_list.head.value}')
# linked_list.add_to_head(5)
# print(f'the start of the list is {linked_list.head.value}')
#
# linked_list.remove_head()
# print(f'the start of the list is {linked_list.head.value}')


linked_list.add_to_head(0)
linked_list.add_to_head(1)
linked_list.add_to_head(2)
linked_list.add_to_head(3)

print(linked_list)