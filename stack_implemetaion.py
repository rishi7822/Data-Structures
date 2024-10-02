#stack implementation
stack = []

#append to push elements
stack.append('a')
stack.append('b')
stack.append('c')

print("Initail Stack")
print(stack)

#pop to remove elements
print('\nElements popped from stack')
print(stack.pop())
print(stack.pop())
print(stack.pop())


print('\nStack after elements are pooped')
print(stack)


#stack with all the operation 
class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty list to store stack elements

    # Function to add an element to the stack (Push operation)
    def push(self, item):
        self.stack.append(item)
        print(f"{item} pushed onto stack")

    # Function to remove and return the top element (Pop operation)
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty"

    # Function to return the top element without removing it (Peek operation)
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty"

    # Function to check if the stack is empty
    def is_empty(self):
        return len(self.stack) == 0

    # Function to return the size of the stack
    def size(self):
        return len(self.stack)

    # Function to display the current stack
    def display(self):
        print("Current stack:", self.stack)

# Driver code to test the Stack implementation
if __name__ == "__main__":
    stack = Stack()

    # Push elements onto the stack
    stack.push(10)
    stack.push(20)
    stack.push(30)
    
    # Display stack contents
    stack.display()

    # Peek at the top element
    print(f"Top element is: {stack.peek()}")

    # Pop elements from the stack
    print(f"Popped element: {stack.pop()}")
    print(f"Popped element: {stack.pop()}")

    # Display stack contents after pop operations
    stack.display()

    # Check if stack is empty
    print(f"Is stack empty? {stack.is_empty()}")

    # Pop the remaining element
    print(f"Popped element: {stack.pop()}")
    
    # Try to pop from an empty stack
    print(f"Popped element: {stack.pop()}")

    # Check stack size
    print(f"Stack size is: {stack.size()}")
