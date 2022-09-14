#Version which finds first occurence of set string in superstring 
# def findMask (arr, str1):
#     #the fisrt one should be by default lower case 
#     for str2 in arr:
#         str3 = str1.upper() #default version
#         i = str3.find(str2)
#         str1 = str1[:i] + str1[i].lower() + str1[i+1:]
#     return str1.swapcase()

#Version which finds all occurences of set string in superstring 
import re
def findMask (arr, str1):
    for str2 in arr:
        str3 = str1.upper() #default version
        i = str3.find(str2)
        occ = [m.start() for m in re.finditer(str2, str3)]
        for i in occ:
            str1 = str1[:i] + str1[i].lower() + str1[i+1:]
    return str1.swapcase()
