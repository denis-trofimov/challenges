#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

class FrequencyTable(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        self.counter = Counter()

    def insert(self, value):
        current = self.get(value)
        if current:
            self[value] = current + 1
            self.counter[current] -= 1
            self.counter[current + 1] += 1
        else:
            self[value] = 1
            self.counter[1] += 1

    def remove(self, value):
        current = self.get(value)
        if current:
            if current == 1:
                self.pop(value)
                self.counter[1] -= 1
            else:
                self[value] = current - 1
                self.counter[current] -= 1
                self.counter[current - 1] += 1                

    def check_exact_frequency(self, frequency):
        return '1' if self.counter[frequency] else '0'

# Complete the freqQuery function below.
def freqQuery(queries):
    frequency_fable = FrequencyTable()
    answers = []
    for query in queries:
        op, value = query
        if op == 1:
            frequency_fable.insert(value)
        elif op == 2:
            frequency_fable.remove(value)
        else:
            answers.append(frequency_fable.check_exact_frequency(value))
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
