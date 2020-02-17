#!/bin/bash

if [ ! -f ./pagerank_reduce ]
then
    g++ -O3 pagerank_reduce.cpp -o pagerank_reduce
fi

./pagerank_reduce
