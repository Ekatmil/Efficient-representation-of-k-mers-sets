#class Aho-Corasick 

from Automaton_Class import *
from HelperFunction_Automaton import *
from string_functions import *
import time

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

            for state1, list_j in list_L.items(): #for each j in L(s)
                if state1 == state:
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
    #H = AddingAdditionalStr (H, forbidden)
    H = HamiltonianSorthelp(H, first, last)
    #H = HamiltonianSort (H)
    return H
    

#set of words and automaton 
#a = ['aha', "aho", 'aa', 'cora', 'aaa', 'aaab', 'ab']
a = ["ttt","act", "tag", "gga", "aga", "cga", "tga", "cca", "ttg"]
#a = ["klaj", "uku"]

def initialization (a, st):   
    A = Aho_Corasick (a)

    (list_L, link_B, pointer_B, state_F) = preprocessing (a, A)

    H = Hamiltonian (list_L, link_B, pointer_B, state_F, A, len(a))
    return H


def SuperStrhelper(a, sorted_list):
    for i in range (0, len(sorted_list) - 1):
        firstStr = sorted_list[i]
        secondStr = sorted_list[i+1]
        (prefix, over, suffix, size) = overlap(a[firstStr], a[secondStr])
        sStr = prefix + over + suffix
        a[secondStr] = sStr
    return a[sorted_list[len(sorted_list) -1]]

def FindSuperStr (arr):
    st = time.time()
    a = list(arr)
    sorted_list = HamiltonianSort(initialization(a, st))

    resultStr = SuperStrhelper (a, sorted_list)

    et = time.time()
    elapsed_time = et - st
    print('Result is in :', elapsed_time, 'seconds')
    return resultStr
