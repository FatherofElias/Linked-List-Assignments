# Task 1

class Node:
    def __init__(self, data):
        self.data = data  # Initialize the data attribute with the provided value
        self.next = None  # Initialize the next attribute to None
        self.prev = None  # Initialize the prev attribute to None

# Example usage:
node1 = Node(10)
print(f"Node data: {node1.data}")
print(f"Next node: {node1.next}")
print(f"Previous node: {node1.prev}")


# Task 2

class DoublyLinkedList:
    def __init__(self):
        self.head = None  # Initialize the head of the list to None
        self.tail = None  # Initialize the tail of the list to None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_node(self, data):
        if self.head is None:
            return
        
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # If the node to be deleted is the head
                    self.head = current.next
                if current == self.tail:  # If the node to be deleted is the tail
                    self.tail = current.prev
                return
            current = current.next

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")

# Task 3 Test Functionality 

# Create an instance of DoublyLinkedList
doubly_linked_list = DoublyLinkedList()

# Test insertion
print("Inserting elements:")
doubly_linked_list.insert_at_end(1)
doubly_linked_list.insert_at_end(2)
doubly_linked_list.insert_at_end(3)
doubly_linked_list.traverse()  # Expected output: 1 <-> 2 <-> 3 <-> None

# Test deletion
print("\nDeleting an element:")
doubly_linked_list.delete_node(2)
doubly_linked_list.traverse()  # Expected output: 1 <-> 3 <-> None

# Test inserting after deletion
print("\nInserting more elements:")
doubly_linked_list.insert_at_end(4)
doubly_linked_list.insert_at_end(5)
doubly_linked_list.traverse()  # Expected output: 1 <-> 3 <-> 4 <-> 5 <-> None

# Test deletion of head
print("\nDeleting the head element:")
doubly_linked_list.delete_node(1)
doubly_linked_list.traverse()  # Expected output: 3 <-> 4 <-> 5 <-> None

# Test deletion of tail
print("\nDeleting the tail element:")
doubly_linked_list.delete_node(5)
doubly_linked_list.traverse()  # Expected output: 3 <-> 4 <-> None
