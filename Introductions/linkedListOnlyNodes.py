# # Nodes
# # ---- Easy way
# # 1. Value - anything strings, integers, objects
# # 2. The Next Node - pointer to the next node
#
#
# class linkedListNode:
#     def __init__(self, value, nextNode=None):
#         self.value = value
#         self.nextNode = nextNode
#
#
# # "3" -> "7" -> "10"
#
# node1 = linkedListNode("3")
# node2 = linkedListNode("7")
# node3 = linkedListNode("10")
#
# node1.nextNode = node2  # node1 -> node2, "3" -> "7"
# node2.nextNode = node3  # node2 -> node3, "7" -> "10"
#
# # node1 -> node2 -> node3
#
# currentNode = node1
# while True:
#     print(currentNode.value, "->", )
#     if currentNode.nextNode is None:
#         print("None")
#         break
#     currentNode = currentNode.nextNode


# More hands on

class linkedListNode2:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode


class linkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = linkedListNode2(value)
        if self.head is None:
            self.head = node
            return

        currentNode2 = self.head
        while True:
            if currentNode2.nextNode is None:
                currentNode2.nextNode = node
                break
            currentNode2 = currentNode2.nextNode

    def printLinkedList(self):
        currentNode = self.head
        while currentNode is not None:
            print(currentNode.value, "->")
            currentNode = currentNode.nextNode
        print("None")

ll = linkedList()
ll.printLinkedList()
ll.insert("3")
ll.printLinkedList()
ll.insert("44")
ll.printLinkedList()
ll.insert("55")
ll.printLinkedList()