#!/usr/bin/env python 3

#class Aho-Corasick 

import queue


class Aho_Corasick:
    def __init__ (self, kmers):
        self.goto = {}
        self.output = {}
        self.fail = {}
        self.kmers = kmers
        self.goto_function()
        self.fail_function()

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


def processing(kmers, automaton):
    list_L = {}
    state_F = {}
    inverse_E = {}
    depth = {}
    link_B = {}

    print ("kmers are: ", kmers)

    for i in range (0, len(kmers)):
        state = 0
        j = 0
        for char in kmers[i]:

            print ("Char is: ", char)

            state = automaton.goto.get((state, char), state and -1)

            print ("State is: ", state)

            list_L[state] = j
            print ("List L is: ", list_L)

            if j == len(kmers[i]) - 1:
                print ("HEAR")
                state_F [i] = state
                inverse_E[state] = i
                print ("State F is: ", state_F)
                print ("Inverse E is: ", inverse_E)
                if state != -1: #state is not leaf 
                    print (state)
                    state_F[i] = 0 
                    print ("State F is: ", state_F)
            j = j + 1
    print (automaton.goto)

    print ("!!!!!!!!!!!!!!!!!!!!")
    queue = []
    depth[0] = 0
    pointer_B = 0
    for (from_state, char), to_state in automaton.goto.items():

            if from_state == 0 and to_state != 0:
                queue.append(to_state)
                automaton.fail[to_state] = 0

    while queue:
        print ("Queue")
        print (queue)
        queue_state = queue.pop(0)
        for (from_state, char), to_state in automaton.goto.items():
            print ("STATES")
            if from_state == queue_state:

                print (queue_state)
                print (to_state)

                queue.append(to_state)
                if depth.get(queue_state) != None:
                    depth[to_state] = int(depth.get(queue_state)) + 1
                else:
                    depth[to_state] = 1
                link_B[to_state] = pointer_B
                pointer_B = to_state
                helper = inverse_E.get(automaton.fail[to_state])
                if helper != None:
                    state_F[helper] = 0
                print ("FAIL FUNCTION: ", automaton.fail[to_state])
                print ("depth is: ", depth)
                print ("link_B is: ", link_B)
    
    return (depth, list_L, link_B, state_F, inverse_E)

a = ['aha', "aho", 'aa', 'cora']
l = "akikiratlea"
A = Aho_Corasick (a)
result = processing (a, A)
print (result)
