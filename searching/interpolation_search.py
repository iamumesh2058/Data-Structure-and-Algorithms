'''
index = low + ((k-arr[low]) * (high-low)) / (arr[high] - arr[low])
'''

def interpolation_search(arr, l, r, key):
    if l <= r and key <= arr[r] and key >= arr[0]:
        m = int(l + ((key - arr[l]) * (r - l))/(arr[r] - arr[l]))
        print(arr[m])
        if arr[m] == key:
            print("Item found.")
            return
        elif arr[m] < key:
            return interpolation_search(arr, l, m-1, key)
        elif arr[m] > key:
            return interpolation_search(arr, m+1, r, key)
    else:
        print("Item not found")
        return
        


my_arr = [i for i in range(1, 200) if i % 2 == 0]
interpolation_search(my_arr, 0, len(my_arr)-1, 27)


'''
Interpolation search formula
index = low + ((key-arr[low])*(high-low))/(arr[high]-arr[low])
'''