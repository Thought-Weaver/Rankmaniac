#!/bin/bash

# Output of 0 indicates no issues.
# Results of algorithm saved in results directory.

mkdir results

for filename in EmailEnron GNPn100p05 Gnutella
do
  echo "Testing ${filename}"
  cp ../local_test_data/${filename}.txt output.txt
  for i in {1..16}
  do
    cp output.txt temp.txt
    python2 pagerank_map.py < temp.txt | sort | python2 pagerank_reduce.py | python2 process_map.py | sort | python2 process_reduce.py > output.txt
  done
  diff ../sols/${filename}.txt <(grep -Eo '[0-9]+$' output.txt) | wc -l
  cp output.txt results/${filename}.txt
done

rm temp.txt output.txt

