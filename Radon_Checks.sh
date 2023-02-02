#!/bin/bash

#Install Radon if required 
str="$(pip list | grep -F radon)"
if [ -z "$str" ];then
    read -p "Permission to install Radon package[Y/n]: " -n 1 -r
    echo    # (optional) move to a new line
    if [[ $REPLY =~ ^[Yy]$ ]];then
    pip install radon
    echo
    else
    echo "Radon package is Required"
    exit
    fi
fi


mkdir -p radon_test
#Compute Cyclomatic complexity for all Python modules
echo -e "https://radon.readthedocs.io/en/latest/commandline.html#the-cc-command\n" > radon_test/test_cc
radon cc -a *.py -s >> radon_test/test_cc

#Compute the Maintainability Index score for all Python files
echo -e "https://radon.readthedocs.io/en/latest/commandline.html#the-mi-command\n" > radon_test/test_mi
radon mi *.py -s > radon_test/test_mi

#Compute Halstead metrics for all Python modules 
echo -e "https://radon.readthedocs.io/en/latest/commandline.html#the-hal-command\n" > radon_test/test_hal
radon hal *.py > radon_test/test_hal

echo "Test Results are stored in directory $(pwd)/radon_test"