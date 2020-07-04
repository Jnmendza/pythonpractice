class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # return all values in the list a --> b --> c --> d --> None
    # How to loop thru the LL
    def __str__(self):
        output = ''
        current_node = self.head  # Create a tracker node variable
        while current_node is not None:  # loop until its NONE
            output += f'{current_node.value} -> '
            current_node = current_node.next_node  # update the tracker node to the next node

        return output

    def print_list(self):
        curr_node = self.head
        while curr_node:
            print(curr_node.value)
            curr_node = curr_node.next_node

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

    def remove_at_pos(self, pos):
        curr = self.head
        if pos == 0:
            self.head = curr.next_node
            curr = None
            return
        prev = None
        count = 1
        while curr and count != pos:
            prev = curr
            curr = curr.next_node
            count += 1

        if curr is None:
            return

        prev.next_node = curr.next_node
        curr = None

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

    def swap_nodes(self, key1, key2):
        if key1 == key2:
            return
        prev1 = None
        curr1 = self.head
        while curr1 and curr1.value != key1:
            prev1 = curr1
            curr1 = curr1.next_node

        prev2 = None
        curr2 = self.head
        while curr2 and curr2.value != key2:
            prev2 = curr2
            curr2 = curr2.next_node
        if not curr1 or not curr2:
            return

        if prev1:
            prev1.next_node = curr2
        else:
            self.head = curr2
        if prev2:
            prev2.next_node = curr1
        else:
            self.head = curr1

        curr1.next_node, curr2.next_node = curr2.next_node, curr1.next_node

    def print_helper(self, node, name):
        if node is None:
            print(name + ": None")
        else:
            print(name + ":" + node.value)

    # Reverse LL A -> B -> C -> D -----> A <- B <- C <- D
    def reverse_iterative(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(curr, prev):
            if not curr:
                return prev
            nxt = curr.next_node
            curr.next_node = prev
            prev = curr
            curr = nxt
            return _reverse_recursive(curr, prev)

        self.head = _reverse_recursive(curr=self.head, prev=None)

    def merge_two_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if p is None:
            return q
        if q is None:
            return p

        if p and q:
            if p.value < q.value:
                s = p
                p = s.next_node
            else:
                s = q
                q = s.next_node
            new_head = s
        while p and q:
            if p.value <= q.value:
                pass
            else:
                s.next_node = q
                s = q
                q = s.next_node

        if not p:
            s.next_node = q
        if not q:
            s.next_node = p

        return new_head

    def remove_dups(self):
        curr= self.head
        prev = None
        dups = dict()
        while curr:
            if curr.value in dups:
                # Remove node:
                prev.next_node = curr.next_node
                curr = None
            else:
                # Not seen element in dups yet
                dups[curr.value] = 1
                prev = curr
            curr = prev.next_node

    def len_iterative(self):
        count = 0
        curr = self.head
        while curr:
            count += 1
            curr = curr.next_node
        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next_node)

    def nth_to_last_node(self, n):
        # Method 1
        total_len = self.len_iterative()
        curr = self.head
        while curr:
            if total_len == n:
                print(curr.value)
                return curr
            total_len -= 1
            curr = curr.next_node

        if curr is None:
            return

        # Method 2: two pointers
        # p = self.head
        # q = self.head
        #
        # count = 0
        # while q and count < n:
        #     q = q.next_node
        #     count += 1
        # if not q:
        #     print( str(n) + "is greater than the number of nodes in list")
        #
        # while p and q:
        #     p = p.next_node
        #     q = q.next_node
        # return p.value
