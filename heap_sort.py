# To heapify a subtree rooted with node i
# n is the size of the heap
def heapify(arr, n, i):
    largest = i    # Initialize largest as root
    left = 2 * i + 1   # Left child
    right = 2 * i + 2  # Right child

    # If left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # If right child exists and is greater than the largest so far
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If largest is not root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        heapify(arr, n, largest)

# Main function to perform heap sort
def heap_sort(arr):
    n = len(arr)

    # Build a maxheap from the input array
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # One by one extract elements from the heap
    for i in range(n - 1, 0, -1):
        # Move current root (largest) to the end
        arr[i], arr[0] = arr[0], arr[i]
        
        # Call heapify on the reduced heap
        heapify(arr, i, 0)

# Function to print the array
def print_list(arr):
    print(" ".join(map(str, arr)))

# Driver code to test the heap sort
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array:")
    print_list(arr)

    heap_sort(arr)

    print("\nSorted array:")
    print_list(arr)
