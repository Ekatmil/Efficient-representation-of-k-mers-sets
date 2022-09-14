#GREEDY APPROXIMATE ALGORITHM FOR FINDING ANY SUPERSTRING

from re import sub
import sys
from string_functions import *

#function that find the shortest superstring 
def findSuperStr (arr):
    
    first_str = arr.pop()
    while len(arr) > 0:
        second_str = arr.pop()
        [prefix, overlap, suffix, resStr] = betterOverlap(first_str, second_str) #found overlap 
        result = prefix + overlap + suffix #new string 
        first_str = result
    
    return first_str 
 
