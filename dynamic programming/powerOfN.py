import math


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


# Power of N , Sx
# int totnum(int X,int N,int num){
# if(pow(num,N)<X)
#     return totnum(X,N,num+1)+totnum(X-pow(num,N),N,num+1);
# else if(pow(num,N)==X)
#     return 1;
# else
#     return 0;
# inclusive stack simulation
def powerofn(n, power, values, index):
    values.append(index)
    part = pow(index, power)
    if pow(index, power) < n:
        ways = powerofn(n, power, values, index + 1) + powerofn(n - part, power, values, index + 1)
        values.pop()
        return ways
    elif pow(index, power) == n:
        print("right: ", values)
        values.pop()
        return 1
    else:
        print("wrong: ", values)

        values.pop()
        return 0


print("top down", powerofn(10, 1, [], 1))

