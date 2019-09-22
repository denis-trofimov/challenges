#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotate_left function below.
def rotate_left(a, d):
    rotated = a[d:]
    rotated.extend(a[:d])
    return rotated

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = rotate_left(a, d)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
