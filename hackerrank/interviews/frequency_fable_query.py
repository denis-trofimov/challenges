#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


# Complete the freqQuery function below.
def freqQuery(queries):
    lookup = Counter()
    frequencies = Counter()
    answers = []
    for query in queries:
        op, value = query
        if op == 1:
            current = lookup[value]
            lookup[value] = current + 1
            frequencies[current] -= 1
            frequencies[current + 1] += 1
        elif op == 2:
            current = lookup[value]
            if current > 0:
                lookup[value] = current - 1
                frequencies[current] -= 1
                frequencies[current - 1] += 1
        else:
            answers.append(1 if frequencies[value] > 0 else 0)
    return answers


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = freqQuery(queries)

    fptr.write('\n'.join(map(str, ans)))
    fptr.write('\n')

    fptr.close()
