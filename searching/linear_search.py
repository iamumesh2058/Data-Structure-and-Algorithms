def linear_search(arr, key):
    for i in arr:
        if i == key:
            print("Item found")
            return
    print("Item not found")
    return


my_arr = [i for i in range(20)]
linear_search(my_arr, -1)