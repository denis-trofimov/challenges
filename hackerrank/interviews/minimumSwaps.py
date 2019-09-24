#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    swaps = 0
    asc = sorted(arr) 
    lut = {v: i for i, v in enumerate(arr)}
    for i, v in enumerate(arr):
        correct = asc[i]
        if correct != v:
            swap_index = lut[correct]
            arr[swap_index], arr[i] = arr[i], arr[swap_index]
            lut[v] = swap_index
            lut[correct] = i
            swaps += 1
    return swaps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
