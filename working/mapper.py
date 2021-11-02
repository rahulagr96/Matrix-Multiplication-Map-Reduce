#!/usr/bin/env python

import sys
row_a = 5
col_b = 5

for line in sys.stdin:
    matrix_version, row, col, value = line.strip().split(",")
    if matrix_version == "A":
        for i in range(0, col_b):
            key = row + "," + str(i)
            print("%s\t%s\t%s" % (key, col, value))
    elif matrix_version == "B":
        for j in range(0, row_a):
            key = str(j) + "," + col
            print("%s\t%s\t%s" % (key, row, value))
