#class Aho-Corasick 

class Aho_Corasick:
    def __init__ (self, kmers):
        self.goto = {}
        self.fail = {0:0}
        self.kmers = kmers
        self.goto_function()
        self.fail_function()

    def isLeaf(self, state):
        for char, extra in enumerate(['A', 'C', 'T','G']):
            if self.goto[state][char] != '':
                return False
        return True

    # def isLeaf(self, state):
    #     return any((state, char) in self.goto for char in ["A", "C", "T", "G"]) == False


    #CONSTRUCTION OF GOTO FUNCTION (Algo 2)
    #Output: goto function in form (i, b) : j where there is an edge b between states i and j 


    def goto_function (self):
        num_states = len(self.kmers)
        self.goto = [[''] * 4 for _ in range(num_states)]
        new_state = 0
        check_count = 0
        done = False

        for kmer in self.kmers:
            if done:
                break
            state = 0
            j = 0
            for char in kmer:
                i = ['A', 'C', 'T', 'G'].index(char)
                res = self.goto[state][i]
                if res == '':
                    break
                state = res
                j += 1
            for char in kmer[j:]:
                check_count = check_count + 1
                if check_count > num_states: 
                    done = True
                    break
                i = ['A', 'C', 'T', 'G'].index(char)
                new_state += 1
                self.goto[state][i] = new_state
            
                state = new_state
     


    # def goto_function(self):
    #     new_state = 0

    #     for kmer in self.kmers:
    #         state = 0
    #     #procedure enter 
    #     # if it is new, than always FAIL and skip to third loop 
    #         j = 0
    #         for char in kmer:
            
    #             res = self.goto.get((state, char), -1)
            
    #             if res == -1:
    #                 break
    #             state = res
    #             j += 1

    #         for char in kmer[j:]:
    #             new_state += 1
    #             self.goto[(state, char)] = new_state #goto (starting state, value of edge) = new state
    #             state = new_state

    #CONSTRUCTION OF FAIL FUNCTION (Algo 3)
    #Output: fail function in form i:j where i is current state and j is where i fails 


    def fail_function(self):
        n = len(self.goto)
        queue = []

      

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
            if queue_state == len(self.goto):
                continue
            
            for char, extra in enumerate(["A", "C", "T", "G"]):
                # print ("INSIDE FOR LOOP INSIDE WHILE LOOP")
                
                res1 = self.goto[queue_state][char]
          
                if res1 != '':
                    queue.append(res1)
                    state = self.fail[queue_state]
                    while True:
                        if state == len(self.goto):
                            break
              
                        res = self.goto[state][char]
                        if res != '' or state == 0:
                            break
                        state = self.fail[state]
                    self.fail[res1] = res
   

    # def fail_function(self):
    #     queue = []

    #     #store all "first" states into the queue 
    #     l = 0
    #     for char in ["A", "C", "T", "G"]:
    #         res1 = self.goto.get((0,char), -1)
    #         if res1 > 0:
    #             queue.append(res1)
    #             self.fail[res1] = 0

    #     #construction of "inside" fails
    #     while queue:
    #         queue_state = queue.pop(0)
            
    #         for char in ["A", "C", "T", "G"]:
    #             res1 = self.goto.get((queue_state, char), -1)
    #             if res1 != -1:
    #                 queue.append(res1)
    #                 state = self.fail[queue_state]
    #                 while True:
    #                     res = self.goto.get((state, char), state and -1)
    #                     if res != -1:
    #                         break
    #                     state = self.fail[state]
    #                 self.fail[res1] = res
