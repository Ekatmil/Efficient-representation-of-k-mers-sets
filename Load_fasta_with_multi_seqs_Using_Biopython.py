from msilib import sequence
from Bio import SeqIO
import time

start_time = time.time()

#GREEDY APPROXIMATE ALGORITHM FOR FINDINF SHORTEST SUPERSTRING

from re import sub
import sys

#function to calculate minimum of two numbers
def min (a,b): 
    if (a>b):
        return b
    else: 
        return a

#find max overlap of two strings
def overlap (str1, str2):
    
    maxOverlap = -sys.maxsize - 1 #default max overlap
    newStr = "" 
    len1 = len(str1)
    len2 = len(str2)
    
    #Str1 is before Str2 in newStr
    for i in range (1, min(len1, len2)):
        subStr1 = str1[-i:] #prefix of str1
        subStr2 = str2[0:i] #suffix of str2
        #match
        if (subStr1 == subStr2): 
            if (maxOverlap < i): 
                maxOverlap = i #new overlap 
                newStr = str1 + str2[-(len2 - i):] #new string 


    #Str1 is after Str2 in newStr
    for i in range (1, min (len1, len2)):
        subStr1 = str1[0:i] #suffix of str1
        subStr2 = str2[-i:] #prefix of str2
        #match
        if (subStr1 == subStr2):
            if (maxOverlap < i):
                maxOverlap = i #new overlap
                newStr = str2 + str1[-(len1 - i):] #new string 
    
    #return pair of maxOverlap and newStr
    return [maxOverlap, newStr]


#function that find the shortest superstring 
def findShortest (arr, leng):
    print ("inside the function")
    while leng != 1:
        Overlap = -sys.maxsize - 1 #max overlap 
        #index of strings that are in overlap 
        first = 0 
        second = 0
        resultStr = "" #the resulting string


        for i in range (0, leng):
            for j in range (i+1, leng):
                [result, resStr] = overlap(arr[i], arr[j]) #get max overlap of two strings from arr

                if (Overlap < result): #check for there is new max overlap 
                    Overlap = result #new max overlap
                    resultStr = resStr #new resulting string
                    first = i #first string in overlap is stored
                    second = j #second string in overlap is stored

        leng = leng - 1 #last string in array will be ignored 

        #if there are no overlaps 
        if ( Overlap == -sys.maxsize -1 ):
            arr[0] = arr [0] + arr[leng] 
        else:
            arr[first] = resultStr #first string is now new string 
            arr[second] = arr[leng] #second string will be ignored

    return arr[0]


fileName = "one_fasta.fa"
seqs = SeqIO.parse(fileName, 'fasta')

arr=[]
for record in seqs:
    arr = arr + list(record.seq)

k = 31
for i in range (0,len(arr) - k + 1):
    for j in range (i+1,i+k):
        arr[i]+=arr[j]


for i in range (len(arr)-k+1, len(arr)):
    arr.pop()    

with open("randomfile.txt", "w") as external_file:
    print ("I am here")
    print (findShortest (arr, len(arr)), file= external_file) 
    external_file.close()

print ("Time is: ", time.time() - start_time)
