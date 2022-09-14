def findMask (arr, str1):
    #the fisrt one should be by default lower case 
    for str2 in arr:
        str3 = str1.upper() #default version
        i = str3.find(str2)
        str1 = str1[:i] + str1[i].lower() + str1[i+1:]
    return str1.swapcase()
