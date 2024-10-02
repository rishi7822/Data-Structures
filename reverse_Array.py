# def reverse_array_extra_array(arr):
#     reversed_arr = arr[::-1]

#     # Print reversed array
#     print("Reversed Array:", end=" ")
#     for i in reversed_arr:
#         print(i, end=" ")

# # Example usage:
# original_arr = [1, 2, 3, 4, 5]
# reverse_array_extra_array(original_arr)




#reversing using while loop]
# def reverse_list(arr):
#     start = 0
#     end = len(arr) - 1
#     while start < end:


#     #swap ele at the start end
#        arr[start],arr[end] = arr[end],arr[start]
#        start += 1
#        end -= 1


# #drivers function

# if __name__ == "__main__":
#     arr = list(map(int,input("Enter the array:").split()))
#     print("original array",arr)

#     reverse_list(arr)

#     print("Reversed_arr", arr)


#built in function method

original_arr= [2,5,7,8,11]

reversed_arr = list(reversed(original_arr))
                    
print(reversed_arr)




