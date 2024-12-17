'''

Linked List is a collection of Nodes

Node is the pair of data and next
    1. data/value
    2. reference to the next node element

    default node --> [data|next]

self.data -> hold the data/value
self.next -> holds the reference to the next node 
self.head -> points to the current node

Operations: 
    1. insert data at the end(append)

        1. create a new node object using the Node class 
        2> check if the self.head exist if not it means the linked list is empty and has no node present

        if:
            no node is present assign the new node object as the head 
        else:
            declare a new variable "current_node" that hold the position of the current pointed node
            as long as the current_node has a next(reference to another node) value i.e the linked list has more nodes ahead
                 

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node

        else:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next
            current_node.next = new_node

    def display(self):
        if self.head is None:
            return "The linked list is empty"

        else:
            current_node = self.head
            while current_node:
                print(current_node.data,end='-->')
                current_node = current_node.next
            print('end')


l1 = LinkedList()

l1.append(10)
l1.append(20)
l1.append(30)

l1.display()