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
def AddingAdditionalStr (H, forbidden):
    from_list = []
    to_list = []
    for ind, bo in forbidden.items():
        print ("Index is: ", ind)
        print ("Boolean is: ", bo)
        if bo == False:
            if H.get(ind) == None: #exist
                from_list.append(ind)
            to_list.append(ind)
    print ("*To List is: ", to_list)
    print ("*From list is: ", from_list)
    while len(from_list) != 0:
        print ("Length of from list is: ", len(from_list))
        for i in to_list:
            print ("I is: ", i)
            if i not in from_list:
                H[from_list[0]] = i
                print ("New H is: ", H)
                from_list.remove(from_list[0])
                to_list.remove(i)
                ("New From list is: ", from_list)
                ("New To list is: ", to_list)
    #NOTE: check this out. If necessary and if enough 
    if len(to_list) >= 2:
        H[to_list[0]] = to_list[1]
    return H