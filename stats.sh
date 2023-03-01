#! /bin/bash -

if [[ ! -e All_Stats.csv ]]; then
    touch All_Stats.csv
    echo "Genome, Output File, Mask Type, Algorithm, K, Length of k-mers Set, Length of SuperString, CPU Time, Wall-clock time, Memory Usage Peak, Test Result" >> All_Stats.csv
fi

echo "Please enter the name of the file with statistics:"
read filename

if [ -f "$filename" ]; then
    info=$(tail -n1 $filename)
    echo $info >> All_Stats.csv
    echo "Statistics is stored in All_Stats"
else
  echo "File does not exist. Please enter a valid file name."
fi
