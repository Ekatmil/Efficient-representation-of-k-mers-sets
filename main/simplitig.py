def extend_simplitig_forwards (K, simpling, k): 
    extending = True
    while extending:
        extending = False
        #q = suffix (simpling, k-1)  #QUESTION 
        q = simpling[0:k-1]

        # print ("Suffix is: ", q)

        for x in ['A', 'C', 'G', 'T']:
            kmer = q+x
            # print ("kmer is: ", kmer)
            if kmer in K:
                extending = True
                simpling = simpling + x #change
                K.remove(kmer)
                break
    return K, simpling 

def extend_simplitig_backwards (K, simpling, k): 
    extending = True
    while extending:
        extending = False
        #q = suffix (simpling, k-1)  #QUESTION 
        q = simpling[-(k-1):]

        for x in ['A', 'C', 'G', 'T']:
            kmer = x+q
            # print ("kmer is: ", kmer)
            if kmer in K:
                extending = True
                simpling = simpling + x #QUESTION 
                K.remove(kmer)
                break
    return K, simpling 


def compute_maximum_simplitig_from_kmer (K, seeding_kmer, k):
    simpling = seeding_kmer

    K, simpling = extend_simplitig_backwards(K, simpling, k)
    # print ("BACKWARD")
    # print (K, simpling)
    K, simpling =  extend_simplitig_forwards(K, simpling, k)
    # print ("FORWARD")
    # print (K, simpling)

    # K, simpling = extend_simpling_backwards(K, simpling)
    # print ("BACKWARD")
    # print (K, simpling)

    # print ("TO RETURN")
    # print (K, simpling)
    return K, simpling

def compute_simplitig (K, k):
    maximal_simplings = []
    while len(K) > 0:
        seeding_kmer = K.pop()
        K, simpling = compute_maximum_simplitig_from_kmer(K, seeding_kmer, k)
        maximal_simplings.append(simpling)
    return maximal_simplings
