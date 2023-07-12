#!/usr/bin/env python 3
import sys
import argparse
import sys
import time
import tracemalloc

from Load_fasta import *
from mask import *

from simplitig import *
from Greedy_AC import *
from tgreedy import *

from testStr import *
from Statistics import *


def call():
    tracemalloc.start()
    def_k = 31
    st1 = time.time()
    st = time.process_time()

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
        '-a',
        '--aho-corasick',
        dest='ahoCorasick',
        help="call for linear-time implementation of Greedy using the Aho_Corasick automaton",
        action="store_true",
        required=False,
    )

    parser.add_argument(
        '-t',
        '--tgreedy',
        dest='tgreedy',
        help="call for TGreedy",
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

    parser.add_argument(
        '-T',
        '--test',
        dest='test',
        help="Run tests on superstr",
        action="store_true",
        required=False,
    )
    parser.add_argument(
        '-S',
        '--stats',
        dest='statistics',
        help="Store stats to csv file",
        type=str,
        required=False,
    )

    config = parser.parse_args(sys.argv[1:])

    #if no algorithm is chosen
    if not (config.simplitig or config.ahoCorasick or config.tgreedy):
        print('Select one of the options for the algorithm.\n')
        parser.print_help()
        parser.exit(0)

    #load fasta
    arr = load(config.k, config.input)
    arr_saved = arr.copy()
    algorithm = ""

    #algorithms
    if config.simplitig == True:
        algorithm = "Simplitig"
        superSet = compute_simplitig(arr, config.k)  #set
        superStr = "".join(superSet)
    elif config.ahoCorasick == True:
        algorithm = "Greedy_AC"
        superSet = FindSuperStr (arr)
        superStr = "".join(superSet)
    elif config.tgreedy == True:
        algorithm = "TGreedy"
        superSet = FindSuperStrTgreedy(arr)
        superStr = "".join(superSet)

    #mask and output 

    mask = ""
    output_name = "Stdout"

    if config.bitstring == True:
        mask = "Binary"
        superStrMask = findMaskBinary(arr_saved, superStr, config.k)
        if (config.output != None):
            output_name = config.output
            output_file = open(config.output, 'w')
            output_file.write(superStr)
            fileMask = open(config.output + ".mask", 'w')
            fileMask.write(superStrMask)
            mask = mask + ": " + config.output + ".mask"
        else:
            print(superStr + "\n" + superStrMask)

    else:
        mask = "Case_Sensitive"
        superStrMask = findMask(arr_saved, superStr, config.k)
        if (config.output != None):
            output_name = config.output
            output_file = open(config.output, 'w')
            output_file.write(superStrMask)
        else:
            print(superStrMask)

    #Test
    if config.test == True:
        print ()
        print("TEST")
        if config.bitstring == True:
            testAll(superStr, list(arr_saved), config.k, superStrMask)

        else:
            testAll(superStrMask, list(arr_saved), config.k)


    #Statistics 
    tm1 = time.time() - st1
    tm = time.process_time() - st
    memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    if config.statistics != None:
        outputStats (config.statistics,
                    config.input,
                    output_name,
                    mask,
                    algorithm,
                    config.k,
                    len(arr_saved),
                    len(superStr),
                    tm,
                    tm1, 
                    memory)

if __name__ == '__main__':
    call()
    
