# Node class for the BST
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary Search Tree class
class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insert a new value into the BST
    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, current, value):
        if value < current.value:
            if current.left is None:
                current.left = Node(value)
            else:
                self._insert_recursive(current.left, value)
        elif value > current.value:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)
        # If the value already exists, do nothing (or handle duplicates)

    # Search for a value in the BST
    def search(self, value):
        return self._search_recursive(self.root, value)

    def _search_recursive(self, current, value):
        if current is None:
            return False
        if current.value == value:
            return True
        elif value < current.value:
            return self._search_recursive(current.left, value)
        else:
            return self._search_recursive(current.right, value)

# Test cases
bst = BinarySearchTree()
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    bst.insert(v)

print("Searching for 60:", bst.search(60))  # True
print("Searching for 25:", bst.search(25))  # False
print("Searching for 80:", bst.search(80))  # True
