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


#Function that adds to path additional non used words
#NOTE: function fails when where are no a such that H[a] != None and forbidden(a) = False
def AddingAdditionalStr (H, forbidden):
    from_list = []
    to_list = []
    for ind, bo in forbidden.items():

        if bo == False:
            if H.get(ind) == None: #exist
                from_list.append(ind)
            to_list.append(ind)

    while len(from_list) != 0:
        for i in to_list:
            if i not in from_list:
                H[from_list[0]] = i
                from_list.remove(from_list[0])
                to_list.remove(i)

    # #NOTE: check this out. If necessary and if enough 
    # if len(to_list) >= 2:
    #     if H.get(to_list[0]) == None and H.get(to_list[1]) != None: #both not keys 
    #      H[to_list[0]] = to_list[1]
    return H

#Function that sorts Hamiltonian path and outpouts list with the order of strings to merge
def HamiltonianSort (H):
    sorted_list = []
    pair = next(iter((H.items())) ) #take the first pair 
    saved = pair[0] #the key of the first takd pair in case if this pair does not continue
    to_add = pair[1]
    sorted_list.append(saved)
    sorted_list.append(to_add)
    del H[saved]

    while len(H) > 0:
        if H.get(to_add) != None:
            to_add_helper = H[to_add]
            del H[to_add]
            to_add = to_add_helper
        else:
            for key, value in H.items():
                still_going = False
                if value == saved:
                    sorted_list.insert(sorted_list.index(value), key)
                    #sorted_list = [key] + sorted_list
                    saved = key
                    del H[saved]
                    still_going = True
                    break
            if still_going != True:
                pair = next(iter((H.items())) ) #take the first pair 
                saved = pair[0] #the key of the first takd pair in case if this pair does not continue
                to_add = pair[1]
                sorted_list.append(saved)
                sorted_list.append(to_add)
                del H[saved]
    print (H)
    return sorted_list 

