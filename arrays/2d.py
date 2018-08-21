def hourglassSum(arr):
    highest = -100000000
    for i in range(0, len(arr) - 2):
        for j in range(0, len(arr[0]) - 2):
            first = arr[0 + i][0 + j]
            second = arr[0 + i][1 + j]
            third = arr[0 + i][2 + j]
            middle = arr[1 + i][1 + j]
            under1 = arr[2 + i][0 + j]
            under2 = arr[2 + i][1 + j]
            under3 = arr[2 + i][2 + j]
            sum = first + second + third + middle + under1 + under2 + under3
            if sum > highest:
                highest = sum
    return highest


array = [[1, 1, 1, 0, 0, 0],
         [0, 1, 0, 0, 0, 0],
         [1, 1, 1, 0, 0, 0],
         [0, 0, 2, 4, 4, 0],
         [0, 0, 0, 2, 0, 0],
         [0, 0, 1, 2, 4, 0]]
print(hourglassSum(array))
