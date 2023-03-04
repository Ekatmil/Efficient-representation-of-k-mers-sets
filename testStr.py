def allKMers(st, lst):
    print ("--CHECKING EXISTENCE OF ALL K_MERS--")
    #initializing 
    st = st.upper()
    lst_dict = {}
    k = len(lst[0])
    #store all kmers to the dictionary in form kmer:false 
    for kmer in lst:
        lst_dict[kmer] = False

    #check if part of string is in the dictionary 
    for i in range(len(st) - k + 1):
        kmer = st[i:i+k]
        if lst_dict.get(kmer) != None:
            lst_dict[kmer] = True 
    
    #check if all the keys in dictionary have value of True
    checker = all(val == True for val in lst_dict.values())
    
    #print result 
    if checker:
        print ("ALL K-MERS ARE IN SUPERSTRING")
        print ("####################")
    else:
        print ("NOT ALL K-MERS ARE IN SUPERSTRING")
        notFound = set()
        for key, value in lst_dict.items():
            if value == False:
                notFound.add(key)
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



