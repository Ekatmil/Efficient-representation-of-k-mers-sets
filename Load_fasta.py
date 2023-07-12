from Bio import SeqIO

def load (k, fileName):
    seqs = SeqIO.parse(fileName, 'fasta')
    arr = set()

    for record in seqs:

        for i in range (0, len(record.seq) - k +1):
            arr.add(str((record.seq[i: i+k]))) 
            
    return arr