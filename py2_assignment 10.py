# Node class for the tree
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

# Binary tree class
class BinaryTree:
    def __init__(self):
        self.root = None

    # Insert a value into the tree (simple insert to build a basic tree)
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
        else:
            if current.right is None:
                current.right = Node(value)
            else:
                self._insert_recursive(current.right, value)

    # In-order traversal: Left -> Root -> Right
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            print(node.value, end=' ')
            self.inorder_traversal(node.right)

    # Pre-order traversal: Root -> Left -> Right
    def preorder_traversal(self, node):
        if node:
            print(node.value, end=' ')
            self.preorder_traversal(node.left)
            self.preorder_traversal(node.right)

    # Post-order traversal: Left -> Right -> Root
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            print(node.value, end=' ')

# Test cases
tree = BinaryTree()
values_to_insert = [50, 30, 70, 20, 40, 60, 80]

for value in values_to_insert:
    tree.insert(value)

print("In-order Traversal:")
tree.inorder_traversal(tree.root)

print("\nPre-order Traversal:")
tree.preorder_traversal(tree.root)

print("\nPost-order Traversal:")
tree.postorder_traversal(tree.root)
