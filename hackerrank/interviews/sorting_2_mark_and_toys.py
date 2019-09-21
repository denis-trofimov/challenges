#!/bin/python3

import math
import os
import random
import re
import sys


def inplace_quick_sort(S, a, b):
    ''' Sort the list from S[a] to S[b] inclusive using the quick-sort algorithm.
        DS & AP p.559 12.3.2 Additional Optimizations for Quick-Sort. 
    '''
    if a >= b: return
    # range is trivially sorted
    pivot = S[b]
    # last element of range is pivot
    left = a
    # will scan rightward
    right = b-1
    # will scan leftward
    while left <= right:
    # scan until reaching value equal or larger than pivot (or right marker)
        while left <= right and S[left] < pivot:
            left += 1
        # scan until reaching value equal or smaller than pivot (or left marker)
        while left <= right and pivot < S[right]:
            right -= 1
        if left <= right:
            # scans did not strictly cross
            S[left], S[right] = S[right], S[left]
            # swap values
            left, right = left + 1, right - 1
            # shrink range

    # put pivot into its final place (currently marked by left index)
    S[left], S[b] = S[b], S[left]
    # make recursive calls
    inplace_quick_sort(S, a, left - 1)
    inplace_quick_sort(S, left + 1, b)

# Complete the maximumToys function below.
def maximumToys(prices, k):
    inplace_quick_sort(prices, 0, len(prices)-1)
    toys = 0
    for toy in prices:
        k -= toy
        if k >= 0:
            toys += 1
        else:
            break
    return toys

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))

    result = maximumToys(prices, k)

    fptr.write(str(result) + '\n')

    fptr.close()
