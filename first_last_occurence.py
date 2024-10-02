# Function to find the first occurrence of the key
def findFirstOccurrence(arr, low, high, key):
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid  # Record index of the first occurrence
            high = mid - 1  # Continue searching in the left half
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

# Function to find the last occurrence of the key
def findLastOccurrence(arr, low, high, key):
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            result = mid  # Record index of the last occurrence
            low = mid + 1  # Continue searching in the right half
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid - 1
    return result

# Driver code
if __name__ == "__main__":
    # Sample sorted array with duplicates
    arr = [5, 6, 7, 8, 8, 8, 9, 10]
    key = int(input("Enter the element to search for: "))

    # Find the first and last occurrence of the key
    first_index = findFirstOccurrence(arr, 0, len(arr) - 1, key)
    last_index = findLastOccurrence(arr, 0, len(arr) - 1, key)

    # Output the result
    if first_index != -1:
        print(f"First occurrence of {key} is at index: {first_index}")
        print(f"Last occurrence of {key} is at index: {last_index}")
    else:
        print(f"Element {key} not found")
