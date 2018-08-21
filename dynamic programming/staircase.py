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


# n stairs
# m steps
def stepPermsnm(n, m):
    return stepmnutil(n, m, {}, [])


# CHECK WHY
def stepmnutil(n, m, mem, out):
    if n in mem:
        return mem[n]
    if n is 0:
        print("right: " + str(out) + "= " + str(sum(n)))
        return 1
    if n < 0:
        print("wrong: " + str(out) + "= " + str(n))
        return 0
    a = 0
    i = 1
    while i <= m and i <= n:
        out.append(i)
        a = a + stepmnutil(n - i, m, mem, out)
        i = i + 1
        out.pop()
    seen[n] = a
    return a


def countWaysUtil(n, m):
    if n <= 1:
        return n
    a = 0
    i = 1
    while i <= m and i <= n:
        a = a + countWaysUtil(n - i, m)
        i = i + 1
    return a


# Returns number of ways to reach s'th stair
def counts(s, m):
    return countWaysUtil(s + 1, m)


def sum(n):
    v = 0
    for value in range(n):
        v += value
    return v


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


seenUNIQUE = {}


def stepPermsUnique(n):
    """
    :type n: int
    :rtype: int
    """
    global steps1
    steps1 = steps1 + 1
    if n < 0:
        return 0
    if n == 0:
        return 1
    if n in seenUNIQUE:
        return 0
    a = stepPermsUnique(n - 1) + stepPermsUnique(n - 2) + stepPermsUnique(n - 3)
    seenUNIQUE[n] = a
    return a


n = 8
verts = {0: 1, -1: 0, -2: 0, -3: 0}

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

# n = 50
# res = stepPermsUnique(n)
# print(res)
# print("steps: unique: " + str(res) + "\n")

n = 8
m = 3
res = stepPermsnm(n, m)
print(res)
print("steps: n and m: " + str(res))

# Driver program
s, m = 8, 3
print("Number of ways =", counts(s, m))
