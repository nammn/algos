def selection(n):
    for i in range(len(n) - 1):
        bigger_v = 0
        index = 0
        for o in range(i, len(n)):
            if n[o] > bigger_v:
                bigger_v = n[o]
                index = o

        temp = n[i]
        n[i] = n[index]
        n[index] = temp
    return n


numbers = [4, 7, 3, 1, 6, 5]
print(selection(numbers))
