# interpolation search implementation using python

def binary_search(arr, l, r, key):
    if l < r and key <= arr[r] and key >= arr[l]:
        m = int(l+ (r-l)//2)
        print(arr[m])
        if arr[m] == key:
            return m
        elif arr[m] > key:
            return binary_search(arr, l, m-1, key)
        elif arr[m] < key:
            return binary_search(arr, m+1, r, key)
    return False

my_arr = [i for i in range(20)]
binary_search(my_arr, 0, len(my_arr)-1, 18)
    