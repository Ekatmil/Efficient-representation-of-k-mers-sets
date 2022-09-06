#! /usr/bin/env python3

import sys

def read_fasta(file_name):
    file = open(file_name)

    seqs = {}
    for line in file:
        if line[0] =='>':
            definition=line.strip()
            #to get rid of the > in the beggining of the line
            definition = definition.replace('>', '')
        else:
            #checks if key is not in dictionary. If not, then adds to keys as empty string
            if definition not in seqs:
                seqs[defline] = ''
            seqs[defline] += line.strip()
    return (seqs)

fileName = "seq_fasta.fa"
seqs = read_fasta(fileName)

with open("newfile.txt", "w") as external_file:
    for defline in seqs:
        print (defline, seqs[defline], file = external_file)
    external_file.close()
