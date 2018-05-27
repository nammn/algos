# binary_search based, returns position
def binary_search(arr, k, low, high):
    middle = int((low + high) / 2)
    if high >= low:
        if arr[middle] == k:
            return middle
        else:
            if arr[middle] > k:
                return binary_search(arr, k, 0, middle - 1)
            else:
                return binary_search(arr, k, middle + 1, high)
    else:
        return 0


numbers = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(numbers, -1, 0, len(numbers) - 1))
