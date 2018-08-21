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
def topDown(n, c, coins, mem):
    if n == 0:
        print("right: ", coins)
        coins.pop()
        return 1
    if n < 0:
        print("wrong: ", coins)
        coins.pop()
        return 0
    key = str(n) + "-" + str(len(c))
    if key in mem:
        coins.pop()
        return mem[key]
    ways = 0
    i = 0
    while i < len(c):
        coins.append(c[i])
        ways = ways + topDown(n - c[i], c[i:], coins, mem)
        i += 1
    if len(coins) != 0:
        coins.pop()
    mem[key] = ways
    return ways


print("top down", topDown(10, [2, 5, 3, 6], [], {}))
print("recursive", getWays(10, [2, 5, 3, 6]))
