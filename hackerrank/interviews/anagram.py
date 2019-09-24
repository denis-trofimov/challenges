#!/bin/python3

import math
import os
import random
import re
import sys

from collections import Counter


# Complete the makeAnagram function below.
def makeAnagram(a, b):
    count_a = Counter(a)
    count_b = Counter(b)
    diff = 0
    checked = set()
    for key, val in count_a.items():
        checked.add(key)
        val_b = count_b[key]
        diff += abs(val - val_b)

    for key, val in count_b.items():
        if key not in checked:
            diff += val        
    
    return diff // 2

# Complete the anagram function below.
def anagram(s):
    n = len(s)
    if n % 2:
        return -1

    return makeAnagram(s[:n // 2], s[n // 2:])

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
