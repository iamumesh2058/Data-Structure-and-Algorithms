# insertion sorting using python programming language

def insertion_sort(arr, n):
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while temp < arr[j] and j >= 0:
            arr[j+1] = arr[j]
            j = j - 1
        arr[j+1] = temp
    return arr


my_arr = [8, 5, 2, 7, 3]
print(insertion_sort(my_arr, len(my_arr)))