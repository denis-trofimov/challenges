#!/bin/python3

import math
import os
import random
import re
import sys

def memoization(func):
    cache = {}

    def wrapper(*args):
        value = cache.get(args)
        if not value:
            value = func(*args)
            cache[args] = value
        return value

    return wrapper

# Complete the steps function below.
@memoization
def steps(n):
    if n == 0:
        return 1
    elif n < 3:
        return n
    else:
        return steps(n-1) + steps(n-2) + steps(n-3)   

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = steps(n)

        fptr.write(str(res) + '\n')

    fptr.close()
