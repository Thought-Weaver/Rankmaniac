#!/usr/bin/env python

import sys
import heapq

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
    key, value = line.strip("\n").split("\t")
    if key == "iter_num":
        i = int(value)
    else:
        # Append a (rank, key) tuple to be sorted by heapq.
        ranks.append((float(value.split()[0]), key))
        all_lines.append(line)

if i >= MAX_ITER:
    top_k_pages = heapq.nlargest(TOP_K, ranks)
    for tup in top_k_pages:
        sys.stdout.write("FinalRank:%f\t%s\n" % tup)
else:
    sys.stdout.write("iter_num\t%d\n" % (i + 1))
    for line in all_lines:
        sys.stdout.write(line)