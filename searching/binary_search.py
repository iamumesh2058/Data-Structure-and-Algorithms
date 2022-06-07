
def binary_search(arr, l, r, key):
    if l <= r:
        m = int((l+r)/2)
        if arr[m] == key:
            print("Item found.")
            return
        elif arr[m] < key:
            return binary_search(arr, l, m-1, key)
        elif arr[m] > key:
            return binary_search(arr, m+1, r, key)
    else:
        print("Item not found")
        return
        


my_arr = [i for i in range(1, 9)]
binary_search(my_arr, 0, len(my_arr), 5)