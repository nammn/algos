steps = 0
steps1 = 0
stei = 0
nway = 0


def stepPerms(n, seen):
    """
    :type n: int
    :rtype: int
    """
    global steps
    steps = steps + 1
    if n in seen:
        return seen[n]
    a = stepPerms(n - 1, seen) + stepPerms(n - 2, seen) + stepPerms(n - 3, seen)
    seen[n] = a
    return a


seen = {0: 1, -1: 0, -2: 0, -3: 0}


def stepPerms1(n):
    """
    :type n: int
    :rtype: int
    """
    global steps1
    steps1 = steps1 + 1
    if n in seen:
        return seen[n]
    a = stepPerms1(n - 1) + stepPerms1(n - 2) + stepPerms1(n - 3)
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


n = 300
verts = {0: 1, -1: 0, -2: 0, -3: 0}
#
# res = it(n)
# print(res)
# print("steps: rek " + str(stei) + "\n")

res = stepPerms(n, verts)
print(res)
print("steps mem1: " + str(steps) + "\n")

res = stepPerms1(n)
print(res)
print("steps mem global: " + str(steps1) + "\n")

res = countWays(n)
print(res)
print("steps: tabulation: " + str(nway) + "\n")
