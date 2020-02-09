#!/usr/bin/env python

import sys
import heapq

alpha = 0.85

# So, the current plan, since we want to extract the top 20 items is simply to
# use heapq and its lovely nlargest functionality.

TOP_K = 20

# I'm going to make the stopping criterion around 15 iterations -- that should
# be enough to converge to the best 20 pages given that alpha = 0.85.
MAX_ITER = 15

ranks = []  # Keep a list of the pageranks
all_lines = []  # Keep a list of all lines to be passed if need be
i = 0  # Current iteration

for line in sys.stdin:
    key, value = line.split("\t")
    if key == "iter_num":
        i = int(value)
    else:
        # Append a (rank, key) tuple to be sorted by heapq.
        value = value.split(',', 1) # [rank, outlinks]
        ranks.append(((float(value[0]), value[1]), key))
        all_lines.append(line)

if i >= MAX_ITER:
    top_k_pages = heapq.nlargest(TOP_K, ranks,
            lambda x : x[0][0])
    for k,v in top_k_pages:
        sys.stdout.write("FinalRank:{}\t{}\n".format(k[0], v))
else:
    sys.stdout.write("iter_num\t%d\n" % (i + 1))
    for k,v in ranks:
        sys.stdout.write("{}\t{},{}".format(v, k[0], k[1]))
