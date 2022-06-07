def ternary_search(arr, l, r, key):
    if l <= r:
        mid1 = l + (r-l)//3
        mid2 = r - (r-l)//3
        
        if arr[mid1] == key:
            return mid1
        if arr[mid2] == key:
            return mid2
        if key < arr[mid1]:
            return ternary_search(arr, l, mid1-1, key)
        elif key > arr[mid2]:
            return ternary_search(arr, mid2+1, r, key)
        else:
            return ternary_search(arr, mid1+1, mid2-1, key)
    return False


my_arr = [i for i in range(20)]
x = 15
index = ternary_search(my_arr, 0, len(my_arr)-1, x)
if index:
    print("Item present")
else:
    print("Item is not present")