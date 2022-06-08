def merge(arr, start, end):
    i = j = k = 0
    while i < len(start) and j < len(end):
        if start[i] < end[j]:
            arr[k] = start[i]
            i += 1
        else:
            arr[k] = end[j]
            j += 1
        k += 1
        
    while i < len(start):
        arr[k] = start[i]
        i += 1
        k += 1

    while j < len(end):
        arr[k] = end[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        start = arr[:mid]
        end = arr[mid:]
        merge_sort(start)
        merge_sort(end)
        
        merge(arr, start, end)
            
    
if __name__ == "__main__":
    arr = [6, 5, 4, 8, 1, 9]
    # arr = [8, 5, 2, 7, 3]
    merge_sort(arr)
    for i in range(len(arr)):
        print(arr[i], end=' ')
    print()
        