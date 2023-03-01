def allKMers(st, lst):
    print ("--CHECKING EXISTENCE OF ALL K_MERS--")
    st_helper = st.upper()
    checker = True
    notFound = set()
    Found = set()
    for i in range(len(lst)):
        kmer = lst[i]
        res = st_helper.find(kmer)
        if res == -1:
            checker = False
            notFound.add(kmer)
        elif st[res].islower() and res not in Found:
            print("K-mer", kmer, "is found but is not in the mask")
        else:
            Found.add(res)

    notFound = notFound - Found
    if notFound == False:
        checker == True

    #print checker result
    if checker:
        print ("ALL K-MERS ARE IN SUPERSTRING")
        print ("####################")
    else:
        print ("NOT ALL K-MERS ARE IN SUPERSTRING")
        print ("MISSING: ", *notFound, sep = " ")

    return checker

def noDifferentStr(st, lst, k):
    lst = set(lst)
    checker = True
    print("--CHECKING FOR FALSE K-MERS--")
    for i, char in enumerate(st):
        if i <= len(st) - k and char.isupper():
            word = st[i:i+k].upper()
            if word not in lst:
                print("FALSE K-MER:", word, "UNDER INDEX", i)
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



