class Node:
    def __init__(self, data):
        self.data = data # storing the value in the node
        self.next = None # initially the node doesn't point to anything

class Linkedlist:
    def __init__(self):
        self.head = None # the list starts empty

    def append(self, data):
        new_node = Node(data) # create a new node with the given data

        if self.head is None:
            self.head = new_node # if the list is empty, make the new node the head
        else:
            current = self.head # start at the head
            while current.next: # keep moving to the next node until we reach the last one
                current = current.next
            current.next = new_node # set the last nodes next to the new node

    def prepend(self, data):
        new_node = Node(data) # create a new node with the given data
        new_node.next = self.head # point the new nodes next to the current head
        self.head = new_node # update the head to the new node

    def remove(self, data):
        if self.head and self.head.data == data: # if the head contains the data
            self.head = self.head.next # remove it by updating head
            return
        current = self.head
        while current.next: #transverse the list
            if current.next.data == data: # found the node to remove
                current.next = current.next.next # skip the node
                return
            current = current.next

    def print_list(self):
        current = self.head # start at the head of the list
        while current: # keep going until we reach the end
            print(current.data, end=" -> ") # print the data of the current node
            current = current.next # move to the next node
        print("None") # indicates the end of the list

linked_list = Linkedlist()
linked_list.append(10)
linked_list.append(20)
linked_list.prepend(5)
linked_list.print_list()

print("Before removing:")
linked_list.print_list()

linked_list.remove(20)  # removing a middle element
print("After removing 20:")
linked_list.print_list()

linked_list.remove(5)  # removing the head
print("After removing 5:")
linked_list.print_list()

linked_list.remove(50)  # trying to remove a non-existent element