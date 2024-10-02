#linked list

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

#creating node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

#connecting nodes to form a list
node1.next = node2
node2.next = node3
node3.next = node4

#printing the linked list
current = node1
while current:
    print(current.data)
    current = current.next
    

#single linked list
# Python Function to traverse and print the elements of the linked list
def traverse_linked_list(head):
    # Start from the head of the linked list
    current = head

    # Traverse the linked list until reaching the end (None)
    while current is not None:

        # Print the data of the current node followed by a space
        print(current.data),

        # Move to the next node
        current = current.next

    print() 


#searching
# Python function to search for a value in the Linked List
def search_linked_list(head, target):

    # Traverse the Linked List
    while head is not None:

        # Check if the current node's data matches the target value
        if head.data == target:

            return True  # Value found
        # Move to the next node
        head = head.next

    return False  # Value not found

#inseritng at begin
# Python function to insert a new node at the beginning of the
# linked list
def insert_at_beginning(head, value):
  
    # Create a new node with the given value
    new_node = Node(value)

    # Set the next pointer of the new node to the current
    # head
    new_node.next = head

    # Move the head to point to the new node
    head = new_node

    # Return the new head of the linked list
    return head

#inserting at end
# Python function to insert a node at the end of the linked
# list
def insert_at_end(head, value):
  
    # Create a new node with the given value
    new_node = Node(value)

    # If the list is empty, make the new node the head
    if head is None:
        return new_node

    # Traverse the list until the last node is reached
    current = head
    while current.next is not None:
        current = current.next

    # Link the new node to the current last node
    current.next = new_node

    return head


#deleting 
# Python Function to remove the first node
# of the linked list
def removeFirstNode(head):
    if not head:
        return None
    temp = head

    # Move the head pointer to the next node
    head = head.next
    temp = None
    return head
