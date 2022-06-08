# bubble sort using python

def bubble_sort(arr, n):
    for i in range(0, n-1):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


my_arr = [9, 2, 8, 7, 3, 1, 4, 6, 5]
print(bubble_sort(my_arr, len(my_arr)))