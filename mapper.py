#!/usr/bin/env python
import sys
for line in sys.stdin:
    line = line.strip()
    entry = line.split(",")
    key = entry[0]
    value = line
    if key == 'A':
        print('{0}\t{1}'.format(key, value))
    elif key == 'B':
        print('{0}\t{1}'.format(key, value))
