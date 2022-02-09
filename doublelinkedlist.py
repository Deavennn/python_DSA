class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleList:
    def __init__(self):
        self.head = None
    def push(self,new_val):
        newnode = Node(new_val)
        newnode.next = self.head
        if self.head is not None:
            self.head.prev = newnode
        self.head = newnode

    def print(self,node):
        while (node is not None):
            print(node.data),
            last = node
            node = node.next

list = DoubleList()
for i in range(1,11):
    list.push(i)
list.print(list.head)