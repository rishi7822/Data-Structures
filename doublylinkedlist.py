# Python Program to insert a node at the beginning of doubly
# linked list


class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

# Function to insert a new node at the front of doubly linked list
def insert_at_front(head, new_data):
    
    # Create a new node
    new_node = Node(new_data)

    # Make next of new node as head
    new_node.next = head

    # Change prev of head node to new node
    if head is not None:
        head.prev = new_node

    # Return the new node as the head of the doubly linked list
    return new_node

def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end='')
        curr = curr.next
    print()  
    
if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 2 <-> 3 <-> 4
    head = Node(2)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end='')
    print_list(head)

    # Insert a new node at the front of the list
    print("After inserting Node at the front:", end='')
    data = 1
    head = insert_at_front(head, data)

    # Print the updated list
    print_list(head)


#insett node at any place
# Python Program to insert a node after a given node of doubly linked list

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

def insert_after(head, key, new_data):
    curr = head

    # Iterate over Linked List to find the key
    while curr is not None:
        if curr.data == key:
            break
        curr = curr.next

    # If curr becomes None, the given key is not found in the linked list
    if curr is None:
        return head

    # Create a new node
    new_node = Node(new_data)

    # Set prev of new node to the given node
    new_node.prev = curr

    # Set next of new node to the next of the given node
    new_node.next = curr.next

    # Update next of the given node to new node
    curr.next = new_node

    # Update the prev of new node's next with the new node
    if new_node.next is not None:
        new_node.next.prev = new_node

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(f" {curr.data}", end='')
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 1 <-> 3 <-> 4
    head = Node(1)
    head.next = Node(3)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List:", end='')
    print_list(head)

    # Insert a new node after node with data 1
    print("Inserting Node with data 2 after node 1 :", end='')
    data = 2
    key = 1
    head = insert_after(head, key, data)

    # Print the updated list
    print_list(head)

#inserting at any postion
# Python Program to insert a node at a given position

class Node:
    def __init__(self, new_data):
        self.data = new_data
        self.next = None
        self.prev = None

def insert_at_position(head, pos, new_data):
  
    # Create a new node
    new_node = Node(new_data)

    # Insertion at the beginning
    if pos == 1:
        new_node.next = head

        # If the linked list is not empty, set the prev of head to new node
        if head is not None:
            head.prev = new_node

        # Set the new node as the head of the linked list
        head = new_node
        return head

    curr = head
    
    # Traverse the list to find the node before the insertion point
    for _ in range(1, pos - 1):
        if curr is None:
            print("Position is out of bounds.")
            return head
        curr = curr.next

    # If the position is out of bounds
    if curr is None:
        print("Position is out of bounds.")
        return head

    # Set the prev of new node to curr
    new_node.prev = curr

    # Set the next of new node to next of curr
    new_node.next = curr.next

    # Update the next of current node to new node
    curr.next = new_node

    # If the new node is not the last node, update prev of next node to new node
    if new_node.next is not None:
        new_node.next.prev = new_node

    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 4
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(4)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List: ", end="")
    print_list(head)

    # Insert new node with data 3 at position 3
    print("Inserting Node with data 3 at position 3: ", end="")
    data = 3
    pos = 3
    head = insert_at_position(head, pos, data)

    # Print the updated list
    print_list(head)


#inserting at end
# Python Program to insert a node at the end of doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to insert a new node at the end of the doubly linked list
def insert_end(head, new_data):
      
    # Create a new node
    new_node = Node(new_data)
    
    # If the linked list is empty, set the new node as the head
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        # Set the next of the last node to the new node
        curr.next = new_node
        
        # Set the prev of the new node to the last node
        new_node.prev = curr
    
    return head

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" ")
        curr = curr.next
    print()

if __name__ == "__main__":
  
    # Create a hardcoded doubly linked list:
    # 1 <-> 2 <-> 3 
    head = Node(1)
    head.next = Node(2)
    head.next.prev = head
    head.next.next = Node(3)
    head.next.next.prev = head.next

    # Print the original list
    print("Original Linked List: ", end="")
    print_list(head)

    # Insert a new node with data 4 at the end
    print("Inserting Node with data 4 at the end: ", end="")
    data = 4
    head = insert_end(head, data)

    # Print the updated list
    print_list(head)
\