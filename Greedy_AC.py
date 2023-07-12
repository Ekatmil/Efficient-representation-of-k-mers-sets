from Automaton_Class import *
from Helper_Functions_AC import *
from string_functions import *

# ALGORITHM 1: PREPROCESSING
#Input: set of words (kmers) and AC machine with goto and fail functions

def preprocessing(kmers, automaton):
    list_L = {}  #dictionary L in form a:[b], where a is state and b index of word that "has to go throw this state"
    state_F = {} #dictionary F in form a:b, where a is index of word in the set of words and b is finite state for this word
    inverse_E = {} #dictionary E is inverse of F
    depth = {} # dictionary Depth in form a:b where a is state and b is its depth 
    link_B = {} #linked list; dictionary, where key is the state and its value is successor of the state

    for i in range (0, len(kmers)): 
        state = 0 
        j = 0

        for char in kmers[i]:
            state = automaton.goto.get((state, char), -1) 
            list_L = addMultipleValues (list_L, state, i) 

            if j == len(kmers[i]) - 1: 
                state_F [i] = state 
                inverse_E[state] = i 

                if automaton.isLeaf(state) == False: 
                    state_F[i] = 0 
            j = j + 1

    queue = [0]
    depth[0] = 0
    pointer_B = 0 #integer, which represents the first state in a linked list_b

    while queue:
        queue_state = queue.pop(0) 

        for char in ["A", "C", "T", "G"]:
            res = automaton.goto.get((queue_state, char), -1)

            if res!= -1:
                queue.append(res)

                if depth.get(queue_state) != None:
                    depth[res] = int(depth.get(queue_state)) + 1 
                else:
                    depth[res] = 1

                link_B[res] = pointer_B 
                pointer_B = res 
                helper = inverse_E.get(automaton.fail[res]) 

                if helper != None:
                    state_F[helper] = 0

    return (list_L, link_B, pointer_B, state_F)

# ALGORITHM 2: Construction of H 
#Input: Augmented AC machine for the set of words and results of preprocessing 
def Hamiltonian (list_L, link_B, pointer_B, state_F, automaton, n):
    list_P = {} # Dictionary P in form a: [b], where b is index of word in the set of words and a is state where "this word fails" 
    forbidden = {} # Dictionary forbidden in form a: bool where a is the index of word in the set. a = True if word is subword of other and a = False o/w
    first = {} # Dictionary, which keeps track of the first occurrence of state in the Hamiltonian Path
    last = {} # Dictionary, which keeps track of the last occurrence of state in the Hamiltonian Path
    H = {} #Dictionary for storing Hamiltonian Path 

    forbidden = initializeForbidden(forbidden,n) #initializing all values to False for each word 

    #this loop initializes new dictionaries. 
    for j in range (0, n): 
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

                        if first[i] == j: 
                            
                            if len(list_P[state]) == 1: 
                                break
                            else:
                                i = list_P[state][1] 

                        H[i] = j 
                        forbidden[j] = True
                        helper_list = list_P[state]
                        helper_list.remove(i)
                        list_P[state] = helper_list
                        first[last[j]] = first[i] 
                        last[first[i]] = last[j] 

                        if len(helper_list) == 0:
                            break

            list_P = addMultipleValues (list_P, automaton.fail[state], list_P[state]) 
            
        state = link_B[state] 
    return H
    


#Function that creates automaton and runs two algorithms from above. Outputs path H
def initialization (a):
    A = Aho_Corasick (a)
    (list_L, link_B, pointer_B, state_F) = preprocessing (a, A)
    return Hamiltonian (list_L, link_B, pointer_B, state_F, A, len(a))

#Function that finda the set of several superstrings, which have overlap 0 between each other 
def FindSuperStr (kmers_set):
    lst = list(kmers_set) #set to list 
    outputSet = set() #output set 
    H = initialization (lst)
    single_lst = findSingle(H, len(lst)) # find all nodes of indegree = 0
    outputSet = addtoSet (lst, single_lst, H, outputSet)
    return outputSet

