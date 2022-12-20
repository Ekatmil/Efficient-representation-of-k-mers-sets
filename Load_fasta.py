from Bio import SeqIO
from pickle import FALSE, TRUE
from re import sub
from xml.etree.ElementTree import tostring

def load (k, fileName):
    # start_time = time.time()
    seqs = SeqIO.parse(fileName, 'fasta')
    arr = set()
    for record in seqs:
        for i in range (0, len(record.seq) - k +1):
            arr.add(str((record.seq[i: i+k]))) 
    #print ("Done with Load: ", time.time() - start_time)
    return arr
