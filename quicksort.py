# Partition function that selects a pivot, partitions the array around it
def partition(arr, low, high):
    # Pivot chosen as the middle element
    pivot = arr[(low + high) // 2]
    i, j = low, high
    
    while i <= j:
        # Find element on the left that should be on the right
        while arr[i] < pivot:
            i += 1
        # Find element on the right that should be on the left
        while arr[j] > pivot:
            j -= 1
        if i <= j:
            # Swap elements that are out of place
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    
    return i

# QuickSort function using the partition function
def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the index where the pivot is placed
        pi = partition(arr, low, high)
        
        # Recursively sort the left and right partitions
        quick_sort(arr, low, pi - 1)  # Left side of pivot
        quick_sort(arr, pi, high)     # Right side of pivot

# Function to print the array
def print_array(arr):
    print(" ".join(map(str, arr)))

# Driver code to test the optimized QuickSort
if __name__ == "__main__":
    arr = [10, 7, 8, 9, 1, 5]
    print("Given array:")
    print_array(arr)

    quick_sort(arr, 0, len(arr) - 1)

    print("\nSorted array:")
    print_array(arr)
