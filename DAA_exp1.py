def linear_search(arr, key):
    for i in range (len(arr)):
        if arr[i] == key:
            return i
    return -1

def binary_search(arr, key):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            low = mid + 1
        else:
            high = mid -1
            return -1
        
unsorted_data = [90, 10, 46, 25, 17, 78, 5]
key_ls = 25
result_ls = linear_search(unsorted_data, key_ls)  

sorted_data = [5, 12, 17, 25, 46, 78, 90]
key_bs = 25
result_bs = binary_search(sorted_data, key_bs)

print("Linear Search result:", result_ls)
print("Binary Search result:", result_bs)