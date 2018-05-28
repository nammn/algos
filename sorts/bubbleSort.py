def bubble(n):
    for i in range(len(n)-1):
        for o in range(len(n)-1):
            if n[o] > n[o + 1]:
                temp = n[o + 1]
                n[o + 1] = n[o]
                n[o] = temp
    return n


numbers = [4, 7, 3, 1, 6, 5]
print(bubble(numbers))
