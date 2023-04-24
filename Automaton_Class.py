#class Aho-Corasick 
import math 
class Aho_Corasick:
    def __init__ (self, kmers):
        self.goto = []
        self.fail = []
        self.kmers = kmers
        self.goto_function()
        self.fail_function()

    def isLeaf(self, state):
        for char, extra in enumerate(['A', 'C', 'T','G']):
            if self.goto[state][char] != -1:
                return False
        return True

    # def isLeaf(self, state):
    #     return any((state, char) in self.goto for char in ["A", "C", "T", "G"]) == False


    #CONSTRUCTION OF GOTO FUNCTION (Algo 2)
    #Output: goto function in form (i, b) : j where there is an edge b between states i and j 


    def goto_function (self):
        
        num_states = int(math.pow (len(self.kmers[0]), len(self.kmers))) #mistake. Can not work with larger numbers
        self.goto = [[-1] * 4 for _ in range(num_states)]
        new_state = 0
        
        for kmer in self.kmers:
            state = 0
            j = 0
            for char in kmer:
                i = ['A', 'C', 'T', 'G'].index(char)
                res = self.goto[state][i]
                if res == -1:
                    break
                state = res
                j += 1
            for char in kmer[j:]:
                i = ['A', 'C', 'T', 'G'].index(char)
                new_state += 1
                self.goto[state][i] = new_state
                check_last = (state, i, new_state)
                state = new_state
                split_point = new_state

        self.goto = self.goto[:split_point] #to cut the list when required


    #CONSTRUCTION OF FAIL FUNCTION (Algo 3)
    #Output: fail function in form i:j where i is current state and j is where i fails 


    def fail_function(self):
        n = len(self.goto) + 1
        queue = []
        self.fail = [-1 for _ in range(n)]

        #store all "first" states into the queue 
        l = 0
        for char, extra in enumerate(["A", "C", "T", "G"]):
   
            res1 = self.goto[0][char]
            if res1 > 0:
                queue.append(res1)
                self.fail[res1] = 0

        #construction of "inside" fails
        while queue:
      
            queue_state = queue.pop(0)
            if queue_state >= n-1:
                continue
            
            for char, extra in enumerate(["A", "C", "T", "G"]):
                # print ("INSIDE FOR LOOP INSIDE WHILE LOOP")
                
                res1 = self.goto[queue_state][char]
          
                if res1 != -1:
                    queue.append(res1)
                    state = self.fail[queue_state]
                    while True:
                        res = self.goto[state][char]
                        if res != -1 or state == 0 or state == -1:
                            break
                        state = self.fail[state]
                    self.fail[res1] = res
                    
            for i in range (len(self.fail)):
                if self.fail[i] == -1:
                    self.fail[i] = 0


