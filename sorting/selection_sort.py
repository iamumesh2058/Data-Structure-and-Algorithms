# selection sorting using python programming language

def selection_sort(arr, n):
    for i in range(n):
        p = i
        for j in range(i+1, n):
            if arr[j] < arr[p]:
                p = j
        arr[i], arr[p] = arr[p], arr[i]
    return arr


my_arr = [8, 5, 2, 7, 3]
print(selection_sort(my_arr, len(my_arr)))