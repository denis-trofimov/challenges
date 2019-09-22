#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumping_on_clouds function below.
def jumping_on_clouds(c):
    jumps = 0
    pos = 0
    while pos < len(c) - 1:
        if pos < len(c) - 2 and not c[pos + 2]:
            jumps += 1
            pos += 2
        elif pos < len(c) - 1 and not c[pos + 1]:
            jumps += 1
            pos += 1
        else:
            raise("It is not possible to win the game!")
    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumping_on_clouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
