#!/usr/bin/env python 3

#class Aho-Corasick 

from email.mime import audio
import queue


class Aho_Corasick:
    def __init__ (self, kmers):
        self.goto = {}
        self.output = {}
        self.fail = {}
        self.kmers = kmers
        self.goto_function()
        self.fail_function()

    def isLeaf (self, state):
        for (from_state, char), to_state in self.goto.items():
            if state == from_state:
                print (state)
                return False
        return True


    #CONSTRUCTION OF GOTO FUNCTION (Algo 2)
    #Output: goto function and partially comuted output function

    def goto_function(self):
        new_state = 0

        for kmer in self.kmers:
            state = 0

        #procedure enter 
        # if it is new, than always FAIL and skip to third loop 
            j = 0
            for char in kmer:
                res = self.goto.get((state, char), -1)
            
                if res == -1:
                    break
                state = res
                j += 1

            for char in kmer[j:]:
                new_state += 1
                self.goto[(state, char)] = new_state #goto (starting state, value of edge) = new state
                state = new_state


            self.output[state] = [kmer] #outputs (final state) = original value 


    #CONSTRUCTION OF FAIL FUNCTION (Algo 3)
    #Output: fail function and complete outputs function 

    def fail_function(self):
        queue = []

        #store all "first" states into the queue 
        for (from_state, char), to_state in self.goto.items():

            if from_state == 0 and to_state != 0:
                queue.append(to_state)
                self.fail[to_state] = 0

        #construction of "inside" fails
        while queue:

            queue_state = queue.pop(0)

            for (from_state, char), to_state in self.goto.items():
 
                if from_state == queue_state:
                    queue.append(to_state)
                    state = self.fail[from_state]
       

                    while True:
            
                        res = self.goto.get((state, char), state and -1)
                        if res != -1:
                            break
                        state = self.fail[state]

                    self.fail[to_state] = res

                    self.output.setdefault(to_state, []).extend(self.output.get(res, [])) #check this out 
        

def addMultipleValues (dict, key, value):
    if key not in dict:
        dict[key] = list()
    dict[key].append(value)
    return dict

def processing(kmers, automaton):
    list_L = {}
    state_F = {}
    inverse_E = {}
    depth = {}
    link_B = {}

    # print ("kmers are: ", kmers)

    for i in range (0, len(kmers)):
        state = 0
        j = 0
        for char in kmers[i]:
            # print ("J is: ", j)

            # print ("Char is: ", char)

            state = automaton.goto.get((state, char), state and -1)

            # print ("State is: ", state)

            list_L = addMultipleValues (list_L, state, j)
            # print ("List L is: ", list_L)

            if j == len(kmers[i]) - 1:
                # print ("HEAR")
                state_F [i] = state
                inverse_E[state] = i
                # print ("State F is: ", state_F)
                # print ("Inverse E is: ", inverse_E)
                if automaton.isLeaf(state) == False: #state is not leaf or state != -1 
                    # print ("Not leaf situation")
                    # print (automaton.goto.get(2))
                    # print (automaton.goto)
                    # print (state)
                    state_F[i] = 0 
                    # print ("State F is: ", state_F)
            j = j + 1

    # print ("!!!!!!!!!!!!!!!!!!!!")
    queue = [0]
    depth[0] = 0
    pointer_B = 0

    while queue:
        # print ("Queue")
        # print (queue)
        queue_state = queue.pop(0)
        for (from_state, char), to_state in automaton.goto.items():
            # print ("STATES")
            if from_state == queue_state:

                # print ("Queue state: ", queue_state)
                # print ("To state: ", to_state)

                queue.append(to_state)
                if depth.get(queue_state) != None:
                    depth[to_state] = int(depth.get(queue_state)) + 1
                else:
                    depth[to_state] = 1
                # print ("DEPTH: ", depth)

                link_B[to_state] = pointer_B
                pointer_B = to_state
                
                helper = inverse_E.get(automaton.fail[to_state])
                if helper != None:
                    state_F[helper] = 0
                # print ("FAIL FUNCTION: ", automaton.fail[to_state])
                # print ("link_B is: ", link_B)
    
    return (depth, list_L, link_B, pointer_B, state_F, inverse_E, automaton)

def Hamiltonian (list_L, link_B, pointer_B, state_F, automaton, m):
    list_P = {}
    forbidden = {}
    first = {}
    last = {}
    H = []
    print (state_F)
    for j in range (0, m):
        print (j)
        print ("Get j: ", state_F.get(j))
        helper_1 = state_F.get(j)
        if helper_1 != 0:
            print ("here")
            print (automaton.fail.get(helper_1))
            helper = automaton.fail[helper_1]
            print ("helper is: ", helper)
            print (j)
            list_P = addMultipleValues(list_P, helper, j)
            print ("New list is: ", list_P)
            first[j] = last[j] = j 
        else:
            forbidden[j] = True
    
    print ("NEW")
    print (forbidden)

    state = link_B.get(pointer_B)
    print (state)

    while state != 0:
        print (state)
        print (list_P)
        if list_P.get(state) != None:
            for state1, list_j in list_L.items():
                if state1 != state:
                    break
                else: 
                    for j in list_j:
                        #here
                        print (j)
                        print (forbidden.get(j))
                        if forbidden.get(j) != None: 
                            if forbidden[j] == False:
                                i = list_P[state][0]
                                if first[i] == j:
                                    if len(list_P[state]) == 1:
                                        break
                                    else:
                                        i = list_P[state][1]
                                #H = H + {(xi, xj)}
                                H.append()
                                forbidden[j] = True
                                list_P[state] = list_P[state].remove(i)
                                first[last[j]] = first[i]
                                last[first[i]] = last[j]  

            list_P = addMultipleValues (list_P, automaton.fail[state], list_P[state])
        state = link_B[state]    

a = ['aha', "aho", 'aa', 'cora']
l = "akikiratlea"
A = Aho_Corasick (a)
(depth, list_L, link_B, pointer_B, state_F, inverse_E, automaton) = processing (a, A)
Hamiltonian (list_L, link_B, pointer_B, state_F, automaton, 4)

print ("RESULT")
print ("Depth: ", depth)
print ("List L: ", list_L)
print ("b-link: ", link_B)
print ("state F: ", state_F)
print ("inverse of F: ", inverse_E)

               