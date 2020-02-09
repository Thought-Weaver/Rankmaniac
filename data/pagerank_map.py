#!/usr/bin/env python

import sys

# Input: (node i:iteration, [rank(i), list of outlinks])
# Output: (node j:iteration, rank(i) / degree(i))
# Also one line of form (node i:iteration, outlinks(i))

for line in sys.stdin:
    # ==========================================================================
    # Process inputs
    key, value = line.split('\t')

    # Case: this is the ('iter_num', iter_num) pair
    if key[0] == 'i':
        sys.stdout.write(line)
    else:
        node = key
        outlinks = value[:-1].split(',') # Remove newline
        rank = float(outlinks[0])

        # Case: this is first iteration of PageRank.
        if node[0] == 'N':
            node = node[7:] # Remove 'NodeID:'
            outlinks = outlinks[2:] # Remove current and previous PageRank entries
            if len(outlinks) == 0: # Node links to itself if no other outlinks
                outlinks.append(node)

        # Case: not the first iteration.
        else:
            outlinks = outlinks[1:] # Remove PageRank entry

        outlinks_str = ','.join(outlinks)

        # ==========================================================================
        # PageRank
        for outlink in outlinks:
            sys.stdout.write('{}\t{}\n'.format( \
                outlink, \
                rank / len(outlinks)
            ))
            
        # Ensure all nodes are accounted for
        # Also pass on outlinks string
        # 'o' signifies this is outlink tuple
        sys.stdout.write('{}\to{}\n'.format( \
            node, \
            outlinks_str \
        ))

