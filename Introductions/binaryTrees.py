# Root - The topmost node in the tree

# Child - A node directly connected to another node when moving away from the root node.

# Parent - A node directly connected node when moving towards the root node.

# Siblings - Nodes that share the same parent are considered siblings.

# Leaf - A node that does not have any children of its own.

# # Psuedo code
# class BinarySearchTree:
#     self.value = value
#     self.left = left_subtree
#     self.right = right_subtree


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare value to the current node
        # if smaller, go left
        if value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        # if bigger, go right
        elif value > self.value:
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.left.insert(value)

        # if no node to go to, (either left or right)
        elif self.left and self.right is None:
            # make the new node at that spot
            new_node = BinarySearchTree(value)
            return new_node

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # compare target to root
        if target == self.value:
            return True
        # if it's smaller, check left side
        elif target < self.value:
            # first check that there is a left side; if not, return False
            if not self.left:
                return False
            # else, if it doesn't match the left side, call contains on left side with same target
            elif target != self.left:
                return self.left.contains(target)
            else:
                return True
        # else, check right side
        elif target > self.value:
            # first check that there is a right side; if not, return False
            if not self.right:
                return False
            # else, if it doesn't match the right side, call contains on right side with same target
            elif target != self.right:
                return self.right.contains(target)
            else:
                return True

    # Return the maximum value found in the tree
    def get_mx(self):
        if not self:
            return None
        # if we can go right, go right
        # return when we can't go right anymore
        if not self.right:
            return self.value
        max_val = self.right.get_mx()
        return max_val

    # Call the function 'cb' on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)

        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

