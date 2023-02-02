import time
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

# (II) Function that finds the vertices of indegree 0 
# Used in function FindSuperSet

def findSingle (H):
    keys = list(H.keys())
    values = set(H.values())
    output = [x for x in keys if x not in values]
    return output 

# (III) Function to sort dictionary by key in reverse order 
# Used in function Hamiltonian (Note: probably useless)

def sortDict (dict):
    dict1 = {}
    keylist = list(dict.keys())
    keylist.sort()
    for key in keylist[::-1]: #reverse
        dict1[key] = dict[key]
    return (dict1)

#(IV) Function that stores False for every key in "forbidden" dictionary 
# Used in function Hamiltonian 
def initializeForbidden (dict, m):
    for j in range (0, m):
        dict[j] = False
    return dict 

#(V) Function that removes from dictionary with multiple values for one key 
# Could be used in function Hamiltonian (Note: must be checked for correctness)
def removeFromDict (dic, state, i):
    helper_list = dic[state]
    helper_list.remove(i)
    dic[state] = helper_list
    return dic


# (VI) Function that inverts the dictionary such that value is a key and key is a value
# Not used
def InverseDictionary (dic):
    inverse_dic = {}
    for key, value in dic.items():
        inverse_dic[value] = key 
    return inverse_dic

# (VII) Function that adds merged strings into the set 
# Used by function FindSuperSet and is key function
def addtoSet (a, single, H, outputSet):
    for x in single:
        key = x 
        while True:
            if H.get(key) != None:
                value = H[key]
                (prefix, over, suffix, size) = overlap(a[key], a[value])
                sStr = prefix + over + suffix
                a[value] = sStr
                key = value
            else:
                outputSet.add(sStr)
                break
    return outputSet

# (VIII) Function to sort the path H into the list
# Used by alternative functions of AhoCorasick.py
# Quadratic Time
def HamiltonianSort(H, st):
    single = findSingle(H) #list of vertices of indegree 0
    sorted_list = [] #output list of the sorted path
    i = len(single) - 2
    key = single.pop()#the element from the single is taken and removed
    sorted_list.append(key)
    et = time.time()
    elapsed_time = et - st
    print (single)
    print('Hamiltonian Sort prepared for the while loop :', elapsed_time, 'seconds')

    while True:
        if H.get(key) != None:
            value = H[key]
            sorted_list.append(value)
            key = value
        else:
            if i >= 0:
                key = single[i]
                i = i-1
                sorted_list.append(key)
            else:
                break
    return (sorted_list)



#USED BY TGREEDY

#Function takes list of staring indices and path H and outputs the list of order 
def ConnectStr (arr):
    single = findSingle(arr[0])
    H = arr[0]
    C = arr[1]
    for x in single:
        if x not in C:
            C.append(x)

    print (C)
    sorted_list = []
    while len(C) != 0:
        ind = C.pop()
        # print ("Index is: ", ind)
        sorted_list.append(ind)
        key = H.get(ind)
        # print ("Next key from Index is: ", key)
        # print ("Sorted list: ", sorted_list)
        
        while True:
            new_key = H.get(key)
            # print ("New Key is: ", new_key)
            if new_key == None:
                break
            sorted_list.append(key)
            # print ("Sorted list is: ", sorted_list)
            del H[key]
            key = new_key
    print (len(H))
    print (len(sorted_list))
    return sorted_list
