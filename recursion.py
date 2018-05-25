import math


def multOf3(n):
    if n <= 0:
        return 1
    return multOf3(n - 1) * 3


def computeFactorial(number):
    # your code here\
    if number == 1:
        return 1
    else:
        return number * computeFactorial(number - 1)


def power_n(n, x):
    value = int(math.sqrt(n))
    if n == 1:
        print('return')
        return
    if math.pow(value, x) == n:
        print("is true for: {} and {}".format(value, x))
    else:
        print('going -1')
        power_n(value - 1, x)


count = 0


def reverse(s):
    length = len(s)
    global count
    print('count: '+str(count)+' '+s)
    count +=1
    return s + reverse(s[0:length - 1])


# power_n(101, 2)
# print(computeFactorial(5))
print(reverse("hello"))
