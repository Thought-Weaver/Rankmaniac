#!/usr/bin/env python

import sys

"""
Node data is passed in as:

NodeId:current_node_id\tcur_rank,prev_rank,outlink_1,...

Or we might get iter_num\ti where i is the iteration number.

We output the data either as:

NodeId:current_node_id\tcurrent_node_contribution
NodeId:current_node_id\tcur_rank,prev_rank,outlink_1,...

"""

ALPHA = 0.85

for line in sys.stdin:
    key, value = line.strip("\n").split("\t")
    if key != "iter_num":
        values_split = value.split(",")
        cur_rank, prev_rank, outlinks = float(values_split[0]), float(values_split[1]), values_split[2:]

        if len(outlinks) == 0:
            sys.stdout.write("%s\t%f\n" % (key, (cur_rank * ALPHA)))
        else:
            for outlink in outlinks:
                sys.stdout.write("NodeId:%s\t%f\n" % (outlink, (cur_rank * ALPHA / len(outlinks))))
        sys.stdout.write("%s\t%s,%s,%s\n" % (key, cur_rank, prev_rank, ",".join(outlinks)))
