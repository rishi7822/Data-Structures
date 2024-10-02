def deleteByValue(arr, element):
    if element in arr:
        arr.remove(element)
        print(f"Element {element} deleted.")
    else:
        print(f"Element {element} not found:")

#driver code
if __name__ =="__main__":
    arr = list(map(int, input("Enter the array elements separated by spaces: ").split()))

    key = int(input("enter the key:"))


    print("Before Deletion:")


    deleteByValue(arr, key)

    print("After deletion", arr)
