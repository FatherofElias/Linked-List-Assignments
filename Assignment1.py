# Task 1

class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute with the provided value
        self.next = None  # Initialize the next attribute to None

# Example usage:
node1 = Node(10)
print(f"Node data: {node1.data}")
print(f"Next node: {node1.next}")
