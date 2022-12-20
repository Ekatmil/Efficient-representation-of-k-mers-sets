def allKMers(st, lst):
    print ("--CHECKING EXISTENCE OF ALL K_MERS--")
    st_helper = st.upper()
    checker = True
    notFound = []
    for i in range (0, len(lst)):
        res = st_helper.find(lst[i])
        if res == -1:
            checker = False
            notFound.append(lst[i])
        if st[res].islower():
            print ("K-mer ", lst[i], " is found but is not in the mask")
    if checker:
        print ("ALL K-MERS ARE IN SUPERSTRING")
        print ("####################")
    else:
        print ("NOT ALL K-MERS ARE IN SUPERSTRING")
        print ("MISSING: ", *notFound, sep = "; ")

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
    allKMers(st, lst)
    noDifferentStr (st, lst, k)



