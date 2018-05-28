def insertion_sort(n):
    for i in range(1, len(n)):
        position = i
        value = n[i]
        while position > 0 and value < n[position - 1]:
            n[position] = n[position - 1]
            position -= 1
        n[position] = value
    return n


numbers = [4, 7, 3, 1, 6, 5]
print(insertion_sort(numbers))
