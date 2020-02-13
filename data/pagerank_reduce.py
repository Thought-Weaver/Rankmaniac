#!/usr/bin/env python

import sys


ALPHA = 0.85
all_lines = {}

for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    if key == "iter_num":
        sys.stdout.write(line)
    else:
        if all_lines.get(key) is None:
            all_lines[key] = []
        all_lines[key].append(value)

for key, values in all_lines.items():
    sum = 1 - ALPHA
    ranks_and_outlinks = []
    for v in values:
        if "," in v:
            ranks_and_outlinks = v.split(",")
        else:
            sum += float(v)
    # Now that we've summed up the contributions from each outlink,
    # we need to swap the prev and cur rank, then set cur_rank to the sum.
    cur_rank = ranks_and_outlinks[0]
    ranks_and_outlinks[0] = str(sum)
    ranks_and_outlinks[1] = cur_rank

    sys.stdout.write("%s\t%s\n" % (key, ",".join(ranks_and_outlinks)))


