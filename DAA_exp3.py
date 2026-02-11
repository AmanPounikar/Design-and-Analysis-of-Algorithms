#quick sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]  

    left = []
    right = []

    for i in arr[1:]:
        if i <= pivot:
            left.append(i)
        else:
            right.append(i)

    return quick_sort(left) + [pivot] + quick_sort(right)

numbers = [5, 2, 9, 1, 5, 6]
print(quick_sort(numbers))

#merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result

numbers = [5, 2, 9, 1, 5, 6]
print(merge_sort(numbers))