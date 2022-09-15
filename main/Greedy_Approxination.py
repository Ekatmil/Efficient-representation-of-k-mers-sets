#GREEDY APPROXIMATE ALGORITHM FOR FINDING ANY SUPERSTRING

from re import sub
import sys
from string_functions import *


def findSuperStr(arr):

    leng = len(arr)

    while leng != 1:
        Overlap = -sys.maxsize - 1  #max overlap
        #index of strings that are in overlap
        first = 0
        second = 0
        resultStr = ""  #the resulting string

        for i in range(0, leng):
            for j in range(i + 1, leng):
                [prefix, over, suffix, maxOver
                 ] = overlap(arr[i],
                             arr[j])  #get max overlap of two strings from arr
                result = prefix + over + suffix

                if (Overlap < maxOver):  #check for there is new max overlap
                    Overlap = maxOver  #new max overlap
                    resultStr = result  #new resulting string
                    first = i  #first string in overlap is stored
                    second = j  #second string in overlap is stored

        leng = leng - 1  #last string in array will be ignored

        #if there are no overlaps
        if (Overlap == -sys.maxsize - 1):
            arr[0] = arr[0] + arr[leng]
        else:
            arr[first] = resultStr  #first string is now new string
            arr[second] = arr[leng]  #second string will be ignored

    return arr[0]
