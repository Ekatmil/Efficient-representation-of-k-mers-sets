from msilib import sequence
from Bio import SeqIO

fileName = "seq_fasta.fa"
seqs = SeqIO.parse(fileName, 'fasta')

with open("newfile.txt", "w") as external_file:
    for record in seqs:
        print (record.description, record.seq, file = external_file)
    external_file.close()