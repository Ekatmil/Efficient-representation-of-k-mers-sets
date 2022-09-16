def findMask(Kset, str1, k):
    l1 = list(str1)
    for i in range(0, len(l1) - k + 1):
        substr = str1[i:i + k]
        if substr in Kset:
            l1[i] = l1[i].lower()
    StrMask = ''.join(map(str, l1))
    return StrMask.swapcase()


def findMaskBinary(Kset, str1, k):
    l1 = []
    for i in range(0, len(str1) - k + 1):
        substr = str1[i:i + k]
        if substr in Kset:
            l1.append("1")
        else:
            l1.append("0")
    StrMask = ''.join(map(str, l1))
    return StrMask
