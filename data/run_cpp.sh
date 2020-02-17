#!/bin/bash

# Output of 0 indicates no issues.
# Results of algorithm saved in results directory.

mkdir results

for filename in EmailEnron GNPn100p05 Gnutella
do
  echo "Testing ${filename}"
  cp ../local_test_data/${filename}.txt output.txt
  start=$SECONDS
  while :
  do
    echo .
    cp output.txt temp.txt
    ./pagerank_map < temp.txt | sort | ./pagerank_reduce | python2 process_map.py | sort | python2 process_reduce.py > output.txt
    if grep "FinalRank" output.txt > /dev/null 2>&1
    then
      break
    fi
  done
  duration=$(( SECONDS - start ))
  diff ../sols/${filename}.txt <(grep -Eo '[0-9]+$' output.txt) | wc -l
  cp output.txt results/${filename}.txt
  echo "${duration} seconds elapsed"
done

rm temp.txt output.txt
