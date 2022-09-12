#!/usr/bin/env python 3
from json import load
from Bio import SeqIO
import sys
from simplitig import *
from Load_fasta import *
from Greedy_Approxination import *

outputFileExists = False
algo = ""
k = 0
def help():
    print ("Usage:\nmain.py OPTION OPTION... [INPUT_FILE] [OPTIONAL_OUTPUT_FILE]\nOPTIONS:\n -k or -kmer for the k\n -h or --help for the help\n-g or --greedy for the greedy approximation algorithm\n-h or --hamiltonian for the greedy-hamiltonian algorithm\n-s or --simplitig for the simplitig algorithm")
    exit()

args = sys.argv[1:]

#not correct amount arguments
if len(args) <= 2 or len(args) > 5:
    help()

#not provided with k 
elif args[0] != '-k' and args[0] != "--kmer":
    help()

#everything is fine
else:
    k = int(args[1])
    if not args[3].startswith("-"):
        filename = args[3]
    else: 
        help()

    if len(args) == 5:
        output_file = args[4]
        outputFileExists = True

    if args[2] == "-h" or args[2] == "--help":
        help()
    elif args[2] == "-s" or args[2] == "--simplitig":
        algo = "s"
    elif args[2] == "-h" or args[2] == "--hamiltonian":
        algo = "h"
    elif args[2] == "-g" or args[2] == "--greedy":
        algo = "g"
    else:
        help()

#load fasta sequence into the set arr
arr = load(k, filename)

start_time = time.time()
if algo == "s":
    superstr = compute_simplitig(arr, k)
if algo == "g":
    superstr = findShortest(list(arr), len(arr))

print (superstr)
print ("Done with Load: ", time.time() - start_time)

