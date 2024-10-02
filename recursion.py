#recursion
# def factorial(n):
#     if n==0 or n==1:
#         return 1
    
#     #recursive case
#     return n*factorial(n-1)


# print(factorial(5))

# def reverse_list_recursive(arr, start, end):
#     # # Base case: if start index is greater or equal to end index, do nothing
#     if start >= end:
#         return
    

#     #swap the elements from start & end
#     arr[start], arr[end] = arr[end], arr[start]

     
    

#     #  # Recursive call to reverse the inner sublist
#     reverse_list_recursive(arr, start+1, end-1)
    

#     if __name__ == "__main__":
#         arr = list(map(int,input("Enter the array:").split()))

#         print("Original array is:", arr)

#         reverse_list_recursive(arr,0,len(arr-1))

#         print("Reversed array is:",  arr)


#Stack recursion
def reverse_using_Stack(arr):
    #intailize
    stack = arr[:]

    #pop all elements from the stack and push them back to the array

    for i in range(len(arr)):
        arr[i] = stack.pop()

#ex
arr = [23,55,11,2222,1111]
reverse_using_Stack(arr)
print("Reversed array is:", arr)



