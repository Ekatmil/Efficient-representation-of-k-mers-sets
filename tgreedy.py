from Automaton_Class import *
from Greedy_AC import initialization
from Helper_Functions_AC import *
from string_functions import *


# ALGORITHM: Construction of H 
#Input: Augmented AC machine for the set of words and results of preprocessing 
def Hamiltonian (list_L, link_B, pointer_B, state_F, automaton, m):
    list_P = {} # Dictionary P in form a: [b], where b is index of word in the set of words and a is state where "this word fails" 
    forbidden = {} # Dictionary forbidden in form a: bool where a is the index of word in the set. a = True if word is subword of other and a = False o/w
    first = {} 
    last = {}
    H = {}

    forbidden = initializeForbidden(forbidden,m) #initializing all values to False for each word 

    for j in range (0, m): #this lopp initializes new dictionaries. List P is list P(s) = [a], where s is fail state for j in F(a) = j 
        helper_1 = state_F.get(j) #F(j)
        if helper_1 != 0: #F(j) != O
            helper = automaton.fail[helper_1] #f(F(j))
            list_P = addMultipleValues(list_P, helper, j) #P(fail(F(j))) * {j}
            first[j] = last[j] = j # FIRST(j) <- LAST(j) <- j 
        else: #the word is substring 
            forbidden[j] = True 


    state = pointer_B #link_B.get(pointer_B) 
    list_P = sortDict (list_P) #NOTE: check if it even plays any role (probably not)
    while state != 0:
        if list_P.get(state) != None and len(list_P.get(state)) > 0: #if P(s) is not empty 

            list_j = list_L.get(state) 
            for j in list_j:

                if forbidden.get(j) != None: #such that forbidden(j) == False  (word is not subword)
                    if forbidden[j] == False:
                        i = list_P[state][0] #i is the first element of P(s)

                        if first[i] == j: 
                            list_P = removeFromDict (list_P, state, i)
                            forbidden[j] = True
                            break

                                
                        H[i] = j #H <- H * {(Xi, Xj)}
                        forbidden[j] = True

                        first[last[j]] = first[i] # FIRST(LAST(j)) <- FIRST(i)
                        last[first[i]] = last[j] # LAST(FIRST(i)) <- LAST(j)

                    # P(s) <- P(s) - {i}
                        list_P = removeFromDict(list_P, state, i)

                        #NOTE: to prevent IndexError: list index out of range
                        if len(list_P[state]) == 0:
                            break

            #next
            list_P = addMultipleValues (list_P, automaton.fail[state], list_P[state]) # P(fail(s)) <- P(fail(s)) * P(s)

        state = link_B[state]  # s <- b(s)

    return (H)
    
    
#function that find the set of several superstrings, which have overlap 0 between each other 
def FindSuperStrTgreedy (arr):
    a = list(arr) #set to list 
    outputSet = set() #output set 
    H = initialization (a)
    single = findSingle(H, len(arr)) # find all nodes of indegree = 0
    outputSet = addtoSet (a, single, H, outputSet)

    return outputSet
