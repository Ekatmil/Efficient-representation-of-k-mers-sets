def allKMers(st, lst):
    print ("--CHECKING EXISTENCE OF ALL K_MERS--")
    st_helper = st.upper()
    checker = True
    notFound = []
    Found = []
    for i in range (0, len(lst)):
        res = st_helper.find(lst[i])
        if res == -1:
            checker = False
            notFound.append(lst[i])
        elif st[res].islower():
            if Found.find(res) == -1:
                print ("K-mer ", lst[i], " is found but is not in the mask")
        else:
            Found.append(res)
    if checker:
        print ("ALL K-MERS ARE IN SUPERSTRING")
        print ("####################")
    else:
        print ("NOT ALL K-MERS ARE IN SUPERSTRING")
        print ("MISSING: ", *notFound, sep = " ")

    return checker

def noDifferentStr (st, lst, k):
    checker = True
    print ("--CHECKING FOR FALSE K-MERS--")
    for i in range (0, len(st) - k + 1):
        if st[i].isupper():
            word = st[i:i+k]
            word = word.upper()
            if word not in lst:
                print ("FALSE K-MER: ", word, " UNDER INDEX ", i)
                checker = False
    if checker == True:
        print ("THERE ARE NO FALSE K-MERS")
    print ("####################")
    return checker


def applyMask(st, bn):
    print ("--BINARY MASK IS APPLIED--")
    new_st = ""
    for i in range (0, len(st)):
        if int(bn[i]) == 0:
            new_st = new_st + st[i].lower()
        else:
            new_st = new_st + st[i]
    print ("####################")
    return new_st

def testAll(st, lst, k, *bn):
    if bn:
        st = applyMask(st, bn[0])
    checker1 = allKMers(st, lst)
    checker2 = noDifferentStr (st, lst, k)
    if checker1 and checker2:
        return True
    else:
        return False



