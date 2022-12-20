#!/usr/bin/env python 3
from json import load
import sys
import argparse
import sys
from simplitig import *
from Load_fasta import *
from Greedy_Approxination import *
from mask import *
from HelperFunction_Automaton import *
from Automaton_Class import *
from AhoCorasick import *
import time
from testStr import *
#from test import *

def_k = 31
st = time.time()

parser = argparse.ArgumentParser(description="")

parser.add_argument(
    '-k',
    '--kmer',
    dest='k',
    type=int,
    default=def_k,
    help='',
    required=False,
)

parser.add_argument(
    '-s',
    '--simplitig',
    help='call for Simplitig',
    dest='simplitig',
    action="store_true",
    required=False,
)

parser.add_argument(
    '-gh',
    '--hamiltonian',
    help="call for Greedy Hamiltonian",
    dest='hamiltonian',
    action="store_true",
    required=False,
)

parser.add_argument(
    '-g',
    '--greedy',
    dest='greedy',
    help="call for Greedy Approximation",
    action="store_true",
    required=False,
)

parser.add_argument(
    '-a',
    '--aho-corasick',
    dest='ahoCorasick',
    help="call for Aho-Corasick",
    action="store_true",
    required=False,
)

parser.add_argument(
    '-b',
    '--bitstring_mask',
    help="call for bitstring mask",
    dest='bitstring',
    action="store_true",
    required=False,
)

parser.add_argument(
    '-i',
    '--input',
    type=str,
    help="input file",
    dest='input',
    required=True,
)
parser.add_argument(
    '-o',
    '--output',
    dest='output',
    help="optional output file",
    type=str,
    required=False,
)

config = parser.parse_args(sys.argv[1:])

#if no algorithm chosen
if not (config.greedy or config.hamiltonian or config.simplitig or config.ahoCorasick):
    parser.error('No algorithm requested, add -g, -s or -gh')

#load fasta
arr = load(config.k, config.input)
arr_saved = arr.copy()
print ("LENGTH OF LOADED SEQ IS: ", len(arr))

#algorithms
if config.simplitig == True:
    superSet = compute_simplitig(arr, config.k)  #set
    superStr = "".join(superSet)
if config.greedy == True:
    superSet = compute_simplitig(arr, config.k)  #set
    superStr = findSuperStr(superSet)
if config.ahoCorasick == True:
    superStr = FindSuperStr(arr)
if config.hamiltonian == True:
    print("To be updated")

print ("LENGTH OF SUPERSTR IS: ", len(superStr))

#mask and output 

if config.bitstring == True:
    superStrMask = findMaskBinary(arr_saved, superStr, config.k)
    if (config.output != None):
        output_file = open(config.output, 'w')
        output_file.write(superStr)
        output_file.close()
        fileMask = open(config.output + ".mask", 'w')
        fileMask.write(superStrMask)
        fileMask.close()
    else:
        print(superStr + "\n" + superStrMask)

else:
    superStrMask = findMask(arr_saved, superStr, config.k)
    if (config.output != None):
        output_file = open(config.output, 'w')
        output_file.write(superStrMask)
        output_file.close()
    else:
        print(superStrMask)

print ()
print("TEST")
if config.bitstring == True:
    testAll(superStr, list(arr_saved), config.k, superStrMask)
else:
    testAll(superStrMask, list(arr_saved), config.k)