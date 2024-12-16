'''
Every element in the linked list is called Node and it has 2 main things
1. data -> the value
2. next(pointer) -> the next contains the reference to the next node in the linked list
'''
class Node:
    def __init__(self,data):
        self.data = data
        # the next is assigned initailly as None
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        # a new node object is created with the data passed 
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        pointing_node = self.head
        while pointing_node:
            print(pointing_node.data,end="->")
            pointing_node = pointing_node.next
        print("none")