#!/bin/python3

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/new-year-chaos/problem
#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    bribes = 0
    for i, origin in enumerate(q):
        if origin - i -1 > 2:
            print("Too chaotic")
            return
        for bribed in q[max(0, origin - 2):i]:
            if bribed > origin:
                bribes += 1
    print(bribes)
            

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
