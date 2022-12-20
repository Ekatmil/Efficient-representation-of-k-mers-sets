def extend_simplitig_forwards(K, simpling, k):
    extending = True
    while extending:
        extending = False
        q = simpling[-(k - 1):]

        for x in ['A', 'C', 'G', 'T']:
            kmer = q + x
            if kmer in K:
                extending = True
                simpling = simpling + x
                K.remove(kmer)
                break
    return K, simpling


def extend_simplitig_backwards(K, simpling, k):
    extending = True
    while extending:
        extending = False
        q = simpling[0:k - 1]

        for x in ['A', 'C', 'G', 'T']:
            kmer = x + q
            if kmer in K:
                extending = True
                simpling = x + simpling
                K.remove(kmer)
                break
    return K, simpling


def compute_maximum_simplitig_from_kmer(K, seeding_kmer, k):
    simpling = seeding_kmer

    K, simpling = extend_simplitig_backwards(K, simpling, k)
    K, simpling = extend_simplitig_forwards(K, simpling, k)
    return K, simpling


def compute_simplitig(K, k):
    maximal_simplings = []
    while len(K) > 0:
        seeding_kmer = K.pop()
        K, simpling = compute_maximum_simplitig_from_kmer(K, seeding_kmer, k)
        maximal_simplings.append(simpling)
    return maximal_simplings
