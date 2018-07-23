msg = {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H', 9: "I", 10: "J", 11: "K", 12: "L"}


def encode_it(num):
    decoded = ''
    l = len(num)
    i = 0
    while i < l:
        numPart = num[i]
        if i + 1 < l:
            numPart = num[i] + num[i + 1]
        if int(numPart) <= 26:
            decoded += msg[int(numPart)]
            i = i + 2
        else:
            decoded = msg[int(num[i])]
            i += 1
    print(decoded)
    return decoded


encode_it('411111')


def helper(num, l, decode):
    if l <= 0:
        return decode
    numPart = num[0] + num[1]
    if int(numPart) <= 26:
        decode += msg[int(numPart)]
        return helper(num[2:], l - 2, decode)
    else:
        decode += msg[int(num[0])]
        return helper(num[1:], l - 1, decode)


def encode_rek(num):
    print(helper(num, len(num), ""))


encode_rek('411111')
