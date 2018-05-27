def merge(n1, n2):
    len1 = len(n1)
    len2 = len(n2)
    a = []
    c1 = 0
    c2 = 0
    while c1 < len1 and c2 < len2:
        if n1[c1] < n2[c2]:
            a.append(n1[c1])
            c1 += 1
        else:
            a.append(n2[c2])
            c2 += 1
    while c1 < len1:
        a.append(n1[c1])
        c1 += 1
    while c2 < len2:
        a.append(n2[c2])
        c2 += 1
    return a


def merg_sort(a1):
    l1 = len(a1)
    if l1 > 1:
        slices1 = int(l1 / 2)
        middle1 = a1[0:slices1]
        middle2 = a1[slices1:l1]
        left = merg_sort(middle1)
        print('left: ', left)
        right = merg_sort(middle2)
        print('right: ', right)
        print('merged: ', merge(left, right))
        return merge(left, right)


numb = [1, 2, 5, 7]
numb2 = [3, 6, 8]
toSort = [1, 38, 27, 110, 9, 82, 10, 100, 299, 13]

# print(merge(numb, numb2))
merg_sort(toSort)
