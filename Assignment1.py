# Task 1

class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute with the provided value
        self.next = None  # Initialize the next attribute to None

# Example usage:
node1 = Node(10)
print(f"Node data: {node1.data}")
print(f"Next node: {node1.next}")


# Task 2

class SinglyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:  # Traverse to the end of the list
                current = current.next
            current.next = new_node

    def delete_node(self, data):
        if self.head is None:
            return
        
        if self.head.data == data:  # If the head is the node to be deleted
            self.head = self.head.next
            return
        
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        
        if current.next:
            current.next = current.next.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Task 3 Testing functionality 

# Create an instance of SinglyLinkedList
linked_list = SinglyLinkedList()

# Test insertion
print("Inserting elements:")
linked_list.insert_at_end(1)
linked_list.insert_at_end(2)
linked_list.insert_at_end(3)
linked_list.traverse()  # Expected output: 1 -> 2 -> 3 -> None

# Test deletion
print("\nDeleting an element:")
linked_list.delete_node(2)
linked_list.traverse()  # Expected output: 1 -> 3 -> None

# Test inserting after deletion
print("\nInserting more elements:")
linked_list.insert_at_end(4)
linked_list.insert_at_end(5)
linked_list.traverse()  # Expected output: 1 -> 3 -> 4 -> 5 -> None

# Test deletion of head
print("\nDeleting the head element:")
linked_list.delete_node(1)
linked_list.traverse()  # Expected output: 3 -> 4 -> 5 -> None

# Test deletion of tail
print("\nDeleting the tail element:")
linked_list.delete_node(5)
linked_list.traverse()  # Expected output: 3 -> 4 -> None

