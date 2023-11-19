# Circular-Doubly-Linked-List-in-Python
This repository contains a Python implementation of a Circular Doubly Linked List (CDLL). The CDLL is a data structure that consists of a sequence of elements, where each element points to its next and previous element, and the last element points back to the first. The implementation includes basic operations such as insertion at the beginning and end, insertion after a specific node, and deletion of nodes.

Usage:

You can use the provided cdll class to create a Circular Doubly Linked List and perform various operations on it. The display method allows you to print the elements in the list.

python
Copy code
mylist = cdll()
mylist.insert_first(5)
mylist.insert_first(0)
mylist.insert_last(10)
mylist.insert_after(10, 4)
mylist.delete_first()
mylist.delete_last()
mylist.delete_value(5)
mylist.display()
Contribution:

Feel free to contribute to this project by forking the repository and submitting pull requests. If you encounter any issues or have suggestions for improvements, please open an issue.
