#!/bin/python3

import math
import os
import random
import re
import sys


def count_freq(s):
    MAX_VAL = 200 + 1
    # count occurences
    count = [0] * MAX_VAL
    for i in s:
        count[i] += 1
    return count

def median_freq(freq, n):
    median = 0
    if not n % 2:
        stop = n // 2 - 1
    else:
        stop = n // 2
    s = 0
    for k, v in enumerate(freq):
        s += v
        if s > stop:
            if n % 2:
                median = 2 * k
                break
            elif not median:
                stop += 1
                if s > stop:
                    median = 2 * k
                    break
                else:
                    median += k
            else:
                median += k
                break
    return median    

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    if len(expenditure) == d:
        return 0    
    alerts = 0
    start = 0
    end = d
    freq = count_freq(expenditure[start: end])
    while end < len(expenditure):
        if expenditure[end] >= median_freq(freq, d):
            alerts += 1
        freq[expenditure[start]] -= 1
        freq[expenditure[end]] += 1
        start += 1
        end += 1
        
    return alerts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    expenditure = list(map(int, input().rstrip().split()))

    result = activityNotifications(expenditure, d)

    fptr.write(str(result) + '\n')

    fptr.close()
