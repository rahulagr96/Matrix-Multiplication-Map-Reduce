#!/usr/bin/env python
import sys
input_file = open("input.txt").readlines()
for line in input_file:
    line = line.strip()
    entry = line.split(",")
    key = entry[0]
    value = line
    if key == 'A':
        print('{0}\t{1}'.format(key, value))
    elif key == 'B':
        print('{0}\t{1}'.format(key, value))
