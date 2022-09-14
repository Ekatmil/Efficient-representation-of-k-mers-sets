import sys

def overlap (str1, str2):
    
     maxOverlap = -sys.maxsize - 1 #default max overlap
     len1 = len(str1)
     len2 = len(str2)
    
     #Str1 is before Str2 in newStr
     for i in range (1, min(len1 +1 , len2 +1 )): #why +1
         subStr1 = str1[-i:] #prefix of str1
         subStr2 = str2[0:i] #suffix of str2
         #match
         if (subStr1 == subStr2): 
             if (maxOverlap < i): 
                 maxOverlap = i #new overlap 
                 overlapStr = subStr1
                 fix_i = i
     if (maxOverlap == -sys.maxsize -1 ):
        return ["", str1+str2, "", 0]
     if len2 == fix_i:
            return [str1[0:len1 - fix_i], overlapStr, "", maxOverlap]
     else:
        return [str1[0:len1 - fix_i], overlapStr, str2[ -(len2 - fix_i):], maxOverlap]

def betterOverlap (str1, str2):
    resStr1 = overlap (str1, str2)[3]
    resStr2 = overlap (str2, str1)[3]
    if resStr1 >= resStr2:
        return overlap(str1, str2)
    else:
        return overlap(str2, str1)
        
