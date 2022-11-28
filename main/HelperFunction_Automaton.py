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

    # print ("INITIALIZATION")
    # print ("Saved is: ", saved)
    # print ("To add is: ", to_add)
    # print ("New list is: ", sorted_list)
    while len(H) > 0:

        if H.get(to_add) != None:
            # print ("***Add from right")
            to_add_helper = H[to_add]
            sorted_list.append(to_add_helper)
            del H[to_add]
            to_add = to_add_helper
            # print ("New to add is: ", to_add)
            # print ("New list is: ", sorted_list)
        else:
            for key, value in H.items():
                still_going = False
                if value == saved:
                    # print ("***Add from left")
                    sorted_list.insert(sorted_list.index(value), key)
                    #sorted_list = [key] + sorted_list
                    saved = key
                    del H[saved]
                    still_going = True
                    # print ("New saved is: ", saved)
                    # print("New list is: ", sorted_list)
                    break
            if still_going != True:
                # print ("***New cycle")
                pair = next(iter((H.items())) ) #take the first pair 
                saved = pair[0] #the key of the first takd pair in case if this pair does not continue
                to_add = pair[1]
                sorted_list.append(saved)
                sorted_list.append(to_add)
                del H[saved]
                # print ("Saved is: ", saved)
                # print ("To add is: ", to_add)
                # print ("New list is: ", sorted_list)
    return sorted_list 

# def reverseDictionary (dic):
#     reverse_dic = {}
#     for key, value in dic.items():
#         print ("KEY",key)
#         print ("VALUE", value)
#         reverse_dic[value] = key
#         print ("REERSE:", reverse_dic)
#     print (reverse_dic)
#     return (reverse_dic)

# def getToValues (dic1, dic2):
#     print ("Get To Value")
#     print (dic2)
#     print (dic1)
#     dic3 = reverseDictionary(dic2)
#     print (dic1)
#     print (dic3)
#     shared = {k: dic1[k] for k in dic1 if k in dic3 and dic1[k] == dic3[k]}
#     print (shared)




def HamiltonianSorthelp (H, first, last):
    from_array  = [x for x in {k: first[k] for k in first if k in last and first[k] == last[k]}.keys()]
    keys = H.keys()
    values = H.values()
    to_array = [x for x in keys if x not in values]


    while len(from_array) > 0:
        key = from_array.pop(0)
        value = to_array.pop(0)
        H[key] = value
        to_array.append(key)

    return H

    


    # extra_array = []
    # for key, value in last.items():   #of first
    #     if key == value:
    #         if len(to_array) > 0: 
    #             from_v = to_array.pop(0)
    #             H[key] = from_v
    #             extra_array.append(from_v)
    #         else:
    #             extra_array.append(key)

    # if len(to_array) > 0:
    #     extra_array.extend(to_array)
    
    # for i in range (0, len(extra_array) - 1):

    for key, value in first.items():   #of first
        if key == value:
            if key not in from_array:
              from_v = from_array.pop(0)
              H[from_v] = value

              

