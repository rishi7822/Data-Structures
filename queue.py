class Queue:
    def __init__(self, capacity):
        """Initialize the queue with a given capacity."""
        self.front = 0
        self.rear = capacity - 1
        self.size = 0
        self.capacity = capacity
        self.queue = [None] * capacity

    def is_full(self):
        """Check if the queue is full."""
        return self.size == self.capacity

    def is_empty(self):
        """Check if the queue is empty."""
        return self.size == 0

    def enqueue(self, item):
        """Add an item to the queue."""
        if self.is_full():
            print("Queue is full. Cannot enqueue.")
            return
        self.rear = (self.rear + 1) % self.capacity
        self.queue[self.rear] = item
        self.size += 1
        print(f"{item} enqueued to queue")

    def dequeue(self):
        """Remove an item from the queue."""
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return
        dequeued_item = self.queue[self.front]
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        print(f"{dequeued_item} dequeued from queue")

    def front_item(self):
        """Get the front item of the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Front item is {self.queue[self.front]}")

    def rear_item(self):
        """Get the rear item of the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            print(f"Rear item is {self.queue[self.rear]}")

    def display(self):
        """Display the current elements in the queue."""
        if self.is_empty():
            print("Queue is empty.")
        else:
            elements = []
            for i in range(self.size):
                elements.append(self.queue[(self.front + i) % self.capacity])
            print("Queue:", " -> ".join(map(str, elements)))

# Driver Code
if __name__ == "__main__":
    queue = Queue(5)

    # Test enqueue operation
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.enqueue(40)
    queue.enqueue(50)

    # Display the queue
    queue.display()

    # Test dequeue operation
    queue.dequeue()
    queue.display()

    # Check the front and rear items
    queue.front_item()
    queue.rear_item()

    # Try to enqueue another element in a full queue
    queue.enqueue(60)

    # Dequeue remaining elements
    queue.dequeue()
    queue.dequeue()
    queue.display()
