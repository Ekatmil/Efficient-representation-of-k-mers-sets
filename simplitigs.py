# K is the set of k-mers 
# what is simpling?? -> superstring 

k = 3

def extend_simpling_forwards (K, simpling): 
    extending = True
    while extending:
        extending = False
        #q = suffix (simpling, k-1)  #QUESTION 
        q = simpling[0:k-1]

        print ("Suffix is: ", q)

        for x in ['A', 'C', 'G', 'T']:
            kmer = q+x
            print ("kmer is: ", kmer)
            if kmer in K:
                extending = True
                simpling = simpling + x #QUESTION 
                K.discard(kmer)
                break
    return K, simpling 

def extend_simpling_backwards (K, simpling): 
    extending = True
    while extending:
        extending = False
        #q = suffix (simpling, k-1)  #QUESTION 
        q = simpling[-(k-1):]

        print ("Prefix is: ", q)

        for x in ['A', 'C', 'G', 'T']:
            kmer = x+q
            print ("kmer is: ", kmer)
            if kmer in K:
                extending = True
                simpling = simpling + x #QUESTION 
                K.discard(kmer)
                break
    return K, simpling 


def compute_maximum_simpling_from_kmer (K, seeding_kmer):
    simpling = seeding_kmer

    K, simpling = extend_simpling_backwards(K, simpling)
    print ("BACKWARD")
    print (K, simpling)
    K, simpling =  extend_simpling_forwards(K, simpling)
    print ("FORWARD")
    print (K, simpling)

    # K, simpling = extend_simpling_backwards(K, simpling)
    # print ("BACKWARD")
    # print (K, simpling)

    print ("TO RETURN")
    print (K, simpling)
    return K, simpling

def compute_simpling (K):
    maximal_simplings = set()
    while len(K) > 0:
        seeding_kmer = K.pop()
        print ("NODE IS: ", seeding_kmer)
        K, simpling = compute_maximum_simpling_from_kmer(K, seeding_kmer)
        maximal_simplings.add(simpling)

    return maximal_simplings

arr = ["ACG", "CGA", "GAA", "AAG", "AGC", "CGT", "GTA", "TAG", "CGG"]
K = set(arr)

print (compute_simpling(K))
