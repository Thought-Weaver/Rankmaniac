#!/usr/bin/env python

import sys
import heapq

# So, the current plan, since we want to extract the top 20 items is simply to
# use heapq and its lovely nlargest functionality.
TOP_K = 20

# I'm going to make the stopping criterion around 15 iterations -- that should
# be enough to converge to the best 20 pages given that alpha = 0.85.
MAX_ITER = 15

# Also going to try a dynamic stopping condition to see if that's faster than
# a static one? This is the same error as permitted for the 15 iterations,
# so theoretically it won't be that much faster.
THRESHOLD = 0.01

ranks = []  # Keep a list of the pageranks
prev_ranks = []  # Keep a list of the previous pageranks
all_lines = []  # Keep a list of all lines to be passed if need be
i = 0  # Current iteration
running = True  # Boolean to check that process still needs to run

for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    if key == "iter_num":
        i = int(value)
    else:
        # Append a (rank, key) tuple to be sorted by heapq.
        values = value.split(',', 2)  # [rank, prev_rank, outlinks]
        ranks.append((float(value[0]), key))
        prev_ranks.append((float(value[1]), key))
        all_lines.append(line)


cur_top_k = heapq.nlargest(TOP_K, ranks)
prev_top_k = heapq.nlargest(TOP_K, prev_ranks)
percent_diff = sum([abs(prev_top_k[j][0] - cur_top_k[j][0]) / prev_top_k[j][0] for j in range(TOP_K)]) / TOP_K

running = (i >= MAX_ITER or percent_diff <= THRESHOLD)

if running:
    sys.stdout.write("iter_num\t%d\n" % (i + 1))
    for line in all_lines:
        sys.stdout.write(line)
else:
    for r, n in cur_top_k:
        sys.stdout.write("FinalRank:%s\t%s\n" % (r[0], n.split(':')[1]))