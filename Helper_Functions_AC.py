from string_functions import *


# (I) Function to store multiple values with one key in dictionary 
# Used in fucntions Hamiltonian and Preprocessing 

def addMultipleValues (dict, key, value): 
    if key not in dict:
        dict[key] = list()
    if type(value) is list:
        for i in value:
            dict[key].append(i)
    else:
        dict[key].append(value)
    return dict

# (II) Function that finds the words, which are not the H. (indegree 0 and with self overlaps)
# Used in function FindSuperSet and FindSuperSetTgreedy
# n is the length of the kmers set 

def findSingle (H, n):
    keys = list(range(1, n)) 
    values = set(H.values())
    output = [x for x in keys if x not in values]
    return output 


#(III) Function that stores False for every key in "forbidden" dictionary 
# Used in function Hamiltonian
#  
def initializeForbidden (dict, n):
    for j in range (0, n):
        dict[j] = False
    return dict

#(IV) Function that removes from dictionary with multiple values for one key 
# Could be used in function Hamiltonian

def removeFromDict (dict, state, i):
    helper_list = dict[state]
    helper_list.remove(i)
    dict[state] = helper_list
    return dict


# (V) Function that adds merged strings into the set 
# Used by function FindSuperSet and FindSuperSetTgreedy

def addtoSet (kmer_lst, single_lst, H, outputSet):
    for x in single_lst:
        key = x 
        sStr = kmer_lst[x]
        while True:
            if H.get(key) != None:
                value = H[key]
                (prefix, over, suffix, size) = overlap(kmer_lst[key], kmer_lst[value])
                sStr = prefix + over + suffix
                kmer_lst[value] = sStr
                key = value
            else:
                outputSet.add(sStr)
                break
    return outputSet
