# AVLTreeList-Py
 A Python implementation of a balanced list data structure using AVL trees. Efficient operations with O(log n) complexity for search, insertions, and deletions. Ideal for high-performance scenarios.

# AVL Tree Implementation in Python

## Description

This project provides a Python implementation of an AVL (Adelson-Velsky and Landis) tree, which is a self-balancing binary search tree. The AVL tree maintains its height to be logarithmic, ensuring efficient operations for insertion, deletion, and searching in O(log n) time complexity.

## Features

- Insertion: Add new elements to the AVL tree while maintaining balance.
- Deletion: Remove elements from the AVL tree while keeping it balanced.
- Searching: Look up elements efficiently in O(log n) time.
- Height Balancing: Automatic height balancing during insertion and deletion operations.

## Usage

```python
from avl_tree import AVLTree

# Create a new AVL tree
tree = AVLTree()

# Insert elements
tree.insert(42)
tree.insert(18)
tree.insert(66)
# Add more elements...

# Search for an element
result = tree.search(18)
if result:
    print("Element found!")
else:
    print("Element not found.")

# Delete an element
tree.delete(42)

# Display the AVL tree
tree.display()
