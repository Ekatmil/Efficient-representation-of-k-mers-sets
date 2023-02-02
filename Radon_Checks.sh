#!/bin/bash

#Compute Cyclomatic complexity for all Python modules
radon cc -a *.py -s > test_radon_cc

#Compute Halstead metrics for all Python modules 
radon hal *.py > test_radon_hal
