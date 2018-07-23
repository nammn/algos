steps = 0
stei = 0
nway = 0


def stepPerms(n, seen):
    """
    :type n: int
    :rtype: int
    """
    global steps
    steps = steps + 1
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in seen:
        return seen[n]
    a = stepPerms(n - 1, seen) + stepPerms(n - 2, seen) + stepPerms(n - 3, seen)
    seen[n] = a
    return a


def it(n):
    """
    :type n: int
    :rtype: int
    """
    global stei
    stei = stei + 1
    if n < 0:
        return 0
    if n == 0:
        return 1
    a = it(n - 1) + it(n - 2) + it(n - 3)
    return a


def countWays(n):
    res = [0] * (n + 1)
    res[0] = 1
    res[1] = 1
    res[2] = 2

    for i in range(3, n + 1):
        global nway
        nway = nway + 1
        res[i] = res[i - 1] + res[i - 2] + res[i - 3]

    return res[n]


verts = [None] * 500
n = 20

res = it(n)
print(res)
print("steps: " + str(stei) + "\n")

res = stepPerms(n, verts)
print(res)
print("steps : " + str(steps) + "\n")

res = countWays(n)
print(res)
print("steps: " + str(nway) + "\n")
