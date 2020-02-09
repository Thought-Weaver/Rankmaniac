#!/usr/bin/env python

import sys

# Performs collector step in MapReduce
# For use when testing locally

collector = {}

for line in sys.stdin:
    key, value = line.split('\t')
    value = value[:-1] # Remove newline character

    collector[key] = collector.get(key, []) + [value]

for k,v in collector.items():
    sys.stdout.write('{}\t{}\n'.format(k, ','.join(v)))

