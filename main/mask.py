from curses.ascii import isalpha


def findMask(Kset, str1, k):
    l1 = list(str1)
    for i in range(0, len(l1) - k + 1):
        substr = ''.join(map(str, l1[i:(i + k)]))
        if substr in Kset:
            l1[i] = l1[i].lower()
    StrMask = ''.join(map(str, l1))
    return StrMask.swapcase()


def findMaskBinary(Kset, str1, k):
    l1 = list(str1)
    for i in range(0, len(l1) - k + 1):
        substr = ''.join(map(str, l1[i:(i + k)]))
        if substr in Kset:
            l1[i] = "1"
    for i in range(0, len(l1)):
        if l1[i].isalpha():
            l1[i] = "0"
    StrMask = ''.join(map(str, l1))
    return StrMask
