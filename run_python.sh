#!/bin/bash



if (( $# != 2 )); then
    echo "Enter the range of k"
    exit 1
fi

start_x=$1
end_x=$2

z=1

for ((x=start_x; x<=end_x; x++))
do
    for y in a t s
    do
        outfile="out_$z"
        statsfile="stats_$z"
        command="python3 main.py -k $x -${y} -i test_fasta.fa -o $outfile -S $statsfile"
        echo "Command #$z: $command"
        $command
        ((z++))

        mkdir -p outputs
        mv "$outfile" "outputs/$outfile"

        mkdir -p stats
        mv "$statsfile" "stats/$statsfile"
    done
done
