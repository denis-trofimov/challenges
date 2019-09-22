#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeated_string function below.
def repeated_string(s, n):
    a = 0
    indexes = []
    for i, l in enumerate(s, start=1):
        if l == 'a':
            indexes.append(i)

    div = n // len(s)
    rem = n % len(s)
    for i in indexes:
        if rem >= i:
            a += 1
        else:
            break
    a += div * len(indexes)
    return a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeated_string(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
