#!/usr/bin/env python

import sys

# Input: list of (node i, contribution(j) of inlink j)
# Also one line of form (node i, outlinks(i)
# Output: (node i, [rank(i), outlinks(i)])

alpha = 0.85

ranks = []
node = ""
rank = 0.

for line in sys.stdin:
    n,v = line.split('\t')
    
    if n != node:
        if len(node) and n[0] != 'i':
            ranks.append(((rank, outlinks), node))
        node = n
        rank = 0.

    if n[0] == 'i': # This is the iter_num tuple
        sys.stdout.write(line)
    else: # Not iter_num tuple
        if v[0] == 'o': # Outlink tuple
            outlinks = v[1:]
        else:
            rank += float(v)

if len(node) and n[0] != 'i':
    ranks.append(((rank, outlinks), node))
    node = n
    rank = 0.

# Compute PageRank
c = (1 - alpha) / len(ranks)
ranks = [((alpha * r[0] + c, r[1]), n) for r,n in ranks]

# Normalize
norm = sum(r[0]**2 for r,n in ranks)
ranks = [((r[0]/norm, r[1]), n) for r,n in ranks]


for r,n in ranks:
    # Outlinks has a newline
    sys.stdout.write('{}\t{},{}'.format(n, r[0], r[1]))
