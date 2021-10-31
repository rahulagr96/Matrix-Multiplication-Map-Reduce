#!/usr/bin/env python
import sys

a, b = {}, {}
a_row, a_col, b_row, b_col = 0, 0, 0, 0

for input_line in sys.stdin:
    input_line = input_line.strip()

    this_key, value = input_line.split("\t", 1)
    v = value.split(",")

    if this_key == 'A':
        a[(int(v[1]), int(v[2]))] = int(v[3])
        a_row = max(int(v[1]) + 1, a_row)
        a_col = max(int(v[2]) + 1, a_col)
    elif this_key == 'B':
        b[(int(v[1]), int(v[2]))] = int(v[3])
        b_row = max(int(v[1]) + 1, b_row)
        b_col = max(int(v[2]) + 1, b_col)

result = 0
if a_col == b_row:
    for i in range(0, a_row):
        for j in range(0, b_col):
            for k in range(0, a_col):
                result = result + a[(i, k)]*b[(k, j)]
            print("({0},{1})\t{2}".format(i, j, result))
            result = 0
else:
    print("Can not multiply as a_col != b_row")
