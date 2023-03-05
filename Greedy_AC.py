from Automaton_Class import *
from Helper_Functions_AC import *
from string_functions import *

# ALGORITHM 1: PREPROCESSING
#Input: set of words (kmers) and AC machine wirh goto and fail functions

def preprocessing(kmers, automaton):
    list_L = {}  #dictionary L in form a:[b], where a is state and b index of word that "has to go throw this state"
    state_F = {} #dictionary F in form a:b, where a is index of word in the set of words and b is finite state for this word
    inverse_E = {} #dictionary E is inverse of F
    depth = {} # dictionary Depth in form a:b where a is state and b is its depth 
    link_B = {} #linked list 

    for i in range (0, len(kmers)): 
        state = 0 # s <- 0
        j = 0
        for char in kmers[i]:

            state = automaton.goto.get((state, char), state and -1) # s <- goto(s, Aj), where Aj is char 

            list_L = addMultipleValues (list_L, state, i) # L(s) <- L(s) * {j}

            if j == len(kmers[i]) - 1: 
                state_F [i] = state # F(i) <- s
                inverse_E[state] = i # E(s) <- i 

                if automaton.isLeaf(state) == False: #state is not leaf or state != -1 
                    state_F[i] = 0 # F(i) <- 0 

            j = j + 1
    queue = [0]
    depth[0] = 0
    pointer_B = 0

    while queue:
        queue_state = queue.pop(0) #let r be the next state in queue; queue <- queue - r

        for char in ["A", "C", "T", "G"]:
            res = automaton.goto.get((queue_state, char), -1)
            if res!= -1:
                queue.append(res)
                if depth.get(queue_state) != None:
                    depth[res] = int(depth.get(queue_state)) + 1 # d(s) <- d(r) + 1
                else:
                    depth[res] = 1


                link_B[res] = pointer_B #b(s) <- B
                pointer_B = res # B <- s
                
                helper = inverse_E.get(automaton.fail[res]) # F(E(fail(s))) <- 0
                if helper != None:
                    state_F[helper] = 0

    return (list_L, link_B, pointer_B, state_F)

# ALGORITHM 2: Construction of H 
#Input: Augmented AC machine for the set of words and results of preprocessing 
def Hamiltonian (list_L, link_B, pointer_B, state_F, automaton, n):
    list_P = {} # Dictionary P in form a: [b], where b is index of word in the set of words and a is state where "this word fails" 
    forbidden = {} # Dictionary forbidden in form a: bool where a is the index of word in the set. a = True if word is subword of other and a = False o/w
    first = {} 
    last = {}
    H = {}

    forbidden = initializeForbidden(forbidden,n) #initializing all values to False for each word 

    for j in range (0, n): #this lopp initializes new dictionaries. List P is list P(s) = [a], where s is fail state for j in F(a) = j 
        helper_1 = state_F.get(j) #F(j)
        if helper_1 != 0: #F(j) != O
            helper = automaton.fail[helper_1] #f(F(j))
            list_P = addMultipleValues(list_P, helper, j) #P(fail(F(j))) * {j}
            first[j] = last[j] = j # FIRST(j) <- LAST(j) <- j 
        else: #the word is substring 
            forbidden[j] = True 


    state = pointer_B #link_B.get(pointer_B) 


    while state != 0:

        if list_P.get(state) != None and len(list_P.get(state)) > 0: #if P(s) is not empty 

            list_j = list_L.get(state) 
            for j in list_j:

                if forbidden.get(j) != None: #such that forbidden(j) == False  (word is not subword)
                    if forbidden[j] == False:
                        i = list_P[state][0] #i is the first element of P(s)

                        if first[i] == j: 
                            if len(list_P[state]) == 1: #if P(s) has only element then goto next
                                break
                            else:
                                i = list_P[state][1] # i is the second element of P(s)

                        H[i] = j #H <- H * {(Xi, Xj)}
                        forbidden[j] = True

                    # P(s) <- P(s) - {i}
                        helper_list = list_P[state]
                        helper_list.remove(i)
                        list_P[state] = helper_list

                        first[last[j]] = first[i] # FIRST(LAST(j)) <- FIRST(i)
                        last[first[i]] = last[j] # LAST(FIRST(i)) <- LAST(j)

                        #NOTE: to prevent IndexError: list index out of range
                        if len(helper_list) == 0:
                            break

            #next
            list_P = addMultipleValues (list_P, automaton.fail[state], list_P[state]) # P(fail(s)) <- P(fail(s)) * P(s)

        state = link_B[state]  # s <- b(s)
    return H
    


#function that creates automaton and runs two algorithms from above. Outputs path H
def initialization (a):
    A = Aho_Corasick (a)
    (list_L, link_B, pointer_B, state_F) = preprocessing (a, A)
    return Hamiltonian (list_L, link_B, pointer_B, state_F, A, len(a))

#function that find the set of several superstrings, which have overlap 0 between each other 
def FindSuperStr (kmers_set):

    lst = list(kmers_set) #set to list 
    outputSet = set() #output set 
    H = initialization (lst)
    single_lst = findSingle(H, len(lst)) # find all nodes of indegree = 0
    outputSet = addtoSet (lst, single_lst, H, outputSet)

    return outputSet


