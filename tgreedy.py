from Automaton_Class import *
from Greedy_AC import *
from Helper_Functions_AC import *
from string_functions import *


# ALGORITHM: Construction of Cycle Cover
# Input: Augmented AC machine for the set of words and results of preprocessing 
def HamiltonianT (list_L, link_B, pointer_B, state_F, automaton, m):
    list_P = {} # Dictionary P in form a: [b], where b is index of word in the set of words and a is state where "this word fails" 
    forbidden = {} # Dictionary forbidden in form a: bool where a is the index of word in the set. a = True if word is subword of other and a = False o/w
    first = {} # Dictionary, which keeps track of the first occurrence of state in the path
    last = {} # Dictionary, which keeps track of the last occurrence of state in the path
    H = {} #Cycle Cover

    forbidden = initializeForbidden(forbidden,m) #initializing all values to False for each word 

    #this loop initializes new dictionaries. 
    for j in range (0, m):
        helper_1 = state_F.get(j) 

        if helper_1 != 0: 
            helper = automaton.fail[helper_1] 
            list_P = addMultipleValues(list_P, helper, j) 
            first[j] = last[j] = j 
        else: #the word is substring 
            forbidden[j] = True 

    state = pointer_B 

    while state != 0:
        if list_P.get(state) != None and len(list_P.get(state)) > 0: 
            list_j = list_L.get(state) 
            for j in list_j:

                if forbidden.get(j) != None: 
                    if forbidden[j] == False:
                        i = list_P[state][0] 
                        #Cycle
                        if first[i] == j: 
                            list_P = removeFromDict (list_P, state, i)
                            forbidden[j] = True
                            break
      
                        H[i] = j 
                        forbidden[j] = True
                        first[last[j]] = first[i] 
                        last[first[i]] = last[j] 
                        helper_list = list_P[state]
                        helper_list.remove(i)
                        list_P[state] = helper_list
                        if len(helper_list) == 0:
                            break

            list_P = addMultipleValues (list_P, automaton.fail[state], list_P[state]) 
        state = link_B[state]

    return (H)
    

# Function that creates automaton and runs two algorithms. Outputs path H
def initialization (a):
    A = Aho_Corasick (a)
    (list_L, link_B, pointer_B, state_F) = preprocessing (a, A)
    H = HamiltonianT (list_L, link_B, pointer_B, state_F, A, len(a))
    return H
  
# Function that finds the set of several superstrings, which have overlap 0 between each other 
def FindSuperStrTgreedy (arr):
    a = list(arr) #set to list 
    outputSet = set() #output set 
    H = initialization (a)
    single = findSingle(H, len(arr)) # find all nodes of indegree = 0
    outputSet = addtoSet (a, single, H, outputSet) # the MGreedy set
    outputSet_final = FindSuperStr(outputSet) # run Greedy_AC on MGreedy set 
    return outputSet_final