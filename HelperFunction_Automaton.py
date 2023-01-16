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
def sortDict (dict):
    dict1 = {}
    keylist = list(dict.keys())
    keylist.sort()
    for key in keylist[::-1]: #reverse
        dict1[key] = dict[key]
    return (dict1)

#Function that stores False for every key in "forbidden" dictionary 
def initializeForbidden (dict, m):
    for j in range (0, m):
        dict[j] = False
    return dict 

#Function that removes from dictionary with multiple values for one key 
def removeFromDict (dic, state, i):
    helper_list = dic[state]
    helper_list.remove(i)
    dic[state] = helper_list
    return dic

#Used by TGREEDY
#Function takes list of staring indices and path H and outputs the list of order 
def ConnectStr (arr):
    H = arr[0]
    C = arr[1]
    print (C)
    sorted_list = []
    while len(C) != 0:
        ind = C.pop()
        sorted_list.append(ind)
        key = H.get(ind)
        del H[ind]
        
        while True:
            new_key = H.get(key)
            if new_key == None:
                break
            sorted_list.append(key)
            del H[key]
            key = new_key
    return sorted_list

#Function that inverts the dictionary such value is a key and key is a value
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
            # print ("***New cycle")
                pair = next(iter((H.items())) ) #take the first pair 
                saved = pair[0] #the key of the first takd pair in case if this pair does not continue
                to_add = pair[1]
                sorted_list.append(saved)
                sorted_list.append(to_add)
                del H[saved]
                if inverse_H.get(to_add) != None:
                    del inverse_H[to_add]
            # for key, value in H.items(): #inverse of H value^ key 
            #     still_going = False
            #     if value == saved:
            #         # print ("***Add from left")
            #         sorted_list.insert(sorted_list.index(value), key)
            #         #sorted_list = [key] + sorted_list
            #         saved = key
            #         del H[saved]
            #         still_going = True
            #         # print ("New saved is: ", saved)
            #         # print("New list is: ", sorted_list)
            #         break
            # if still_going != True:

                # print ("Saved is: ", saved)
                # print ("To add is: ", to_add)
                # print ("New list is: ", sorted_list)
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

