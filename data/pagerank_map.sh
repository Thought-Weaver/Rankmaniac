#!/bin/bash

if [ ! -f ./pagerank_map ]
then
    g++ -O3 pagerank_map.cpp -o pagerank_map
fi

./pagerank_map
