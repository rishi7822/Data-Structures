def binarySearch (arr, low, high, key):
    while low <= high:
        #calculating the mid point
        mid = (low + high) //2

        #if key is a t mid
        if arr[mid] == key:
            return mid
        
        #if key is greater than mid, dump the left half
        elif arr[mid] < key:
            low = mid + 1

        #if key is smaller than mid, dump the right half
        else:
            high = mid -1

#key not fount
        return -1

#drivers code
if __name__ =="__main__":

    arr = [12,44,16,77,11,22]
    key = int(input("Enter the fucking key:"))

#function calling

result = binarySearch(arr,0,len(arr)-1,key)

if result != 1:
    print(f"Element found at index: {result}")
else:
    print("Element not found")
          

  
    