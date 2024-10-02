# Merge two sorted subarrays arr[left..mid] and arr[mid+1..right]
def merge(arr, left, mid, right):
    # Create temp arrays using slicing
    L = arr[left:mid+1]    # Left subarray
    R = arr[mid+1:right+1] # Right subarray

    i = j = 0  # Initial indices for L and R
    k = left   # Initial index for the merged array

    # Merge the two subarrays back into arr
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy any remaining elements from L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy any remaining elements from R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

# Function that implements Merge Sort
def merge_sort(arr, left, right):
    if left < right:
        mid = (left + right) // 2

        # Recursively sort the first and second halves
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # Merge the sorted halves
        merge(arr, left, mid, right)

# Function to print the array
def print_list(arr):
    print(" ".join(map(str, arr)))

# Driver code
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Given array:")
    print_list(arr)

    merge_sort(arr, 0, len(arr) - 1)

    print("\nSorted array:")
    print_list(arr)
