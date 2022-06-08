# quick sort implementation using pyton

def partition(arr, low, high):
    pivot = arr[high]
    left  = low
    right = high - 1 
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while arr[right] > pivot:
            right -= 1
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
    arr[high], arr[left] = arr[left], arr[high]
    return left

def quick_sort(arr, low, high):
    if low < high:
        par = partition(arr, low, high)
        quick_sort(arr, low, par-1)
        quick_sort(arr, par+1, high)

if __name__ == "__main__":
    arr = [5, 1, 6, 3, 7, 2, 4, 9, 8]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)