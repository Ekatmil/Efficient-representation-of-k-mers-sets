#!/usr/bin/env python 3
from json import load
import sys
import argparse
import sys
from simplitig import *
from Load_fasta import *
from Greedy_Approxination import *
from mask import *

def_k = 31

parser = argparse.ArgumentParser(description="")

parser.add_argument(
    '-k',
    '--kmer',
    dest='k',
    type=int,
    default=def_k,
    help='',
    required=True,
)

parser.add_argument(
    '-s',
    '--simplitig',
    help= 'call for Simplitig',
    dest='simplitig',
    action = "store_true",
    required=False,
)

parser.add_argument(
    '-gh',
    '--hamiltonian',
    help = "call for Greedy Hamiltonian",
    dest='hamiltonian',
    action = "store_true",
    required=False,
)

parser.add_argument(
    '-g',
    '--greedy',
    dest='greedy',
    help = "call for Greedy Approximation",
    action = "store_true",
    required=False,
)

parser.add_argument(
    '-i',
    '--input',
    type=str,
    help = "input file",
    dest='input',
    required=True,
)
parser.add_argument(
    '-o',
    '--output',
    dest='output',
    help = "optional output file",
    type=str ,
    required=False,
)


config = parser.parse_args(sys.argv[1:])

#if no algorithm chosen
if not (config.greedy or config.hamiltonian or config.simplitig):
    parser.error('No algorithm requested, add -g, -s or -gh')
    
#load fasta 
arr = load(config.k, config.input)
arr_saved = arr.copy()

if config.simplitig == True:
    superSet = compute_simplitig (arr, config.k) #set 
    superStr = findSuperStr (superSet)
if config.greedy == True:
    superStr = findSuperStr (arr) #string 
if config.hamiltonian == True:
    print ("To be updated")

superStrMask = findMask(arr_saved, superStr)

#output 
if (config.output != None):
    output_file = open(config.output, 'w')
    output_file.write(superStrMask)
    output_file.close()
else:
    print (superStrMask)

