#!/bin/bash



if (( $# != 3 )); then
    echo "Enter the range of k (start and end) and input file"
    exit 1
fi

start_x=$1
end_x=$2
input_file=$3

mkdir -p outputs
mkdir -p stats

for ((x=start_x; x<=end_x; x++))
do
    for y in a t s
    do
        if [[ $y == "s" ]]; then
            algorithm="simplitig"
        elif [[ $y == "a" ]]; then
            algorithm="Greedy_AC"
        elif [[ $y == "t" ]]; then
            algorithm="Tgreedy"
        else
            echo "Invalid algorithm: $y"
            exit 1
        fi
        z="${input_file}_k${x}_${algorithm}"
        outfile="./outputs/out_$z"
        statsfile="./stats/stats_$z"
        command="python3 main.py -k $x -${y} -i ${input_file} -o $outfile -S $statsfile" 
        echo "Command #$z: $command"
        $command &

    done
done
