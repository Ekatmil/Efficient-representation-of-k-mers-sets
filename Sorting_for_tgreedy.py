# Function to store multiple values with one key 
def addMultipleValues (dict, key, value): 
    if key not in dict:
        dict[key] = list()
    if type(value) is list:
        for i in value:
            dict[key].append(i)
    else:
        dict[key].append(value)
    return dict


#Function to sort dictionary by key in reverse order 
#NOTE: probably useless 
def sortDict (dict):
    dict1 = {}
    keylist = list(dict.keys())
    keylist.sort()
    for key in keylist[::-1]: #reverse
        dict1[key] = dict[key]
    return (dict1)
#Function that store False for every key in "forbidden" dictionary 
def initializeForbidden (dict, m):
    for j in range (0, m):
        dict[j] = False
    return dict 

def InverseDictionary (dic):
    inverse_dic = {}
    for key, value in dic.items():
        inverse_dic[value] = key 
    return inverse_dic

#Function that sorts Hamiltonian path and outpouts list with the order of strings to merge
def HamiltonianSort (H):
    sorted_list = []
    pair = next(iter((H.items())) ) #take the first pair 
    saved = pair[0] #the key of the first takd pair in case if this pair does not continue
    to_add = pair[1]
    sorted_list.append(saved)
    sorted_list.append(to_add)
    del H[saved]
    inverse_H = InverseDictionary(H)

    while len(H) > 0:
        if H.get(to_add) != None:
            # print ("***Add from right")
            to_add_helper = H[to_add]
            sorted_list.append(to_add_helper)
            del H[to_add]
            if inverse_H.get(to_add_helper) != None:
                del inverse_H[to_add_helper]
            to_add = to_add_helper
            # print ("New to add is: ", to_add)
            # print ("New list is: ", sorted_list)
        else:
            still_going = False
            key = inverse_H.get(saved, -1)
            if key != -1:
                sorted_list.insert(sorted_list.index(saved), key)
                saved = key
                del H[saved]
                if inverse_H.get(to_add) != None:
                    del inverse_H[key]
                still_going = True
            
            if still_going != True:     
                pair = next(iter((H.items())) ) #take the first pair 
                saved = pair[0] #the key of the first takd pair in case if this pair does not continue
                to_add = pair[1]
                sorted_list.append(saved)
                sorted_list.append(to_add)
                del H[saved]
                if inverse_H.get(to_add) != None:
                    del inverse_H[to_add]
    return sorted_list 



# A bit faster version than function above
def addToList (dic):
    result = []
    for key, value in dic.items():
        if key == value:
            result.append(key)
    return result

def HamiltonianSorthelp (H, first, last):
    from_array1  = addToList(last)
    from_array2 = addToList (first)
    from_array = list(set(from_array1).intersection(from_array2))

    keys = H.keys()
    values = H.values()
    to_array = [x for x in keys if x not in values]


    while len(from_array) > 0:
        key = from_array.pop(0)
        value = to_array.pop(0)
        H[key] = value
        to_array.append(key)

    return H


def ConnectStr (H, C):
    sorted_list = []
    while len(C) != 0:
        ind = C.pop()
        sorted_list.append[ind]
        key = H.get(ind)
        del H[ind]
        
        while True:
            new_key = H.get(key)
            if new_key == None:
                break
            sorted_list.append[key]
            del H[key]
            key = new_key
    return sorted_list