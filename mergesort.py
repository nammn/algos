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


numb = [1, 2, 5, 7]
numb2 = [3, 6, 8]

print(merge(numb, numb2))
