#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimum_bribes function below.
def minimum_bribes(q):
    dif = 0
    for pos, value in enumerate(q,1):
        if value > pos:
            jump = value - pos
            if jump > 2:
                print("Too chaotic")
                return
        dif += abs(value - pos)
    print(math.ceil(float(dif) / 2))

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
