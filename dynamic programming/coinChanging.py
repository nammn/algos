def getWays(n, c):
    if n == 0:
        return 1
    if n < 0:
        return 0
    value = 0
    i = 0
    while i < len(c):
        value = value + getWays(n - c[i], c[i:])
        i += 1
    return value


# inclusive stack simulation
def topDown(n, c, mem, coins):
    if n == 0:
        print("right: ", coins)
        coins.pop()
        return 1
    if n < 0:
        print("wrong: ", coins)
        coins.pop()
        return 0
    value = 0
    i = 0
    while i < len(c):
        coins.append(c[i])
        value = value + topDown(n - c[i], c[i:], mem, coins)
        i += 1
    mem[n] = value
    coins.pop()
    return mem[n]


mem = {}
print("top down", topDown(10, [2, 5, 3, 6], mem, []))
print(mem)
print("recursive", getWays(10, [2, 5, 3, 6]))
