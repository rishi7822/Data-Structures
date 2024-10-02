#inserting element 
def insertEnd(arr, element):
    arr.append(element)

#drivers code
if __name__ == "__main__":
    arr = list(map(int,input("Enter the array:").split()))

    key = int(input("enter the key:"))



    #array before inserting
    print("Array before inserting:",arr)
    print(arr)

    insertEnd(arr,key)

    print("After Inserting")
    print(arr)