#! /usr/bin/env python3

from msilib import sequence
from Bio import SeqIO
from pickle import FALSE, TRUE
from re import sub
import sys
from xml.etree.ElementTree import tostring
import time

start_time = time.time()


start_time = time.time()

fileName = "one_fasta.fa"
seqs = SeqIO.parse(fileName, 'fasta')

k = 31

arr = []
for record in seqs:
    for i in range (0, len(record.seq) - k +1):
        arr.append(str((record.seq[i: i+k])))

arr = list(dict.fromkeys(arr)) #remove duplicates
print ("Done with Load: ", time.time() - start_time)
