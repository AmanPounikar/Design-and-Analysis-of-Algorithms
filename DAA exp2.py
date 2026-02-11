#insertion sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]          
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr

numbers = [5, 2, 9, 1, 5, 6]
print(insertion_sort(numbers))

#bubble sort
def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

numbers = [5, 2, 9, 1, 5, 6]
print(bubble_sort(numbers))

#selection sort
def selection_sort(arr):
    n = len(arr)

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

numbers = [5, 2, 9, 1, 5, 6]
print(selection_sort(numbers))