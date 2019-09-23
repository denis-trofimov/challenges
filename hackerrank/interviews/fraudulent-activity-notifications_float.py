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
    median = 0.0
    s = 0
    if n % 2 == 1:
        stop = n // 2
        for k, v in enumerate(freq):
            s += v
            if s > stop:
                median = k
                break
    else:
        stop = n // 2 - 1
        for k, v in enumerate(freq):
            s += v
            if s > stop:
                if not median:
                    stop += 1
                    if s > stop:
                        median = k
                        break
                    else:
                        median += k / 2
                else:
                    median += k / 2
                    break
    return median    

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    alerts = 0
    start = 0
    end = d
    freq = count_freq(expenditure[start: end])
    while end < len(expenditure):
        if expenditure[end] >= 2 * median_freq(freq, d):
            alerts += 1
        freq[expenditure[start]] -= 1
        freq[expenditure[end]] += 1
        start += 1
        end += 1
        
    return alerts

if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nd = input().split()

    # n = int(nd[0])

    # d = int(nd[1])
    d = 3
    expenditure = list(map(int, '10 20 30 40 50'.rstrip().split()))
    result = activityNotifications(expenditure, d)
    assert(result == 1)   

    d = 5
    expenditure = list(map(int, '2 3 4 2 3 6 8 4 5'.rstrip().split()))
    result = activityNotifications(expenditure, d)
    assert(result == 2)
    
    d = 4
    expenditure = list(map(int, '1 2 3 4 4'.rstrip().split()))
    result = activityNotifications(expenditure, d)
    assert(result == 0)

    # fptr.write(str(result) + '\n')

    # fptr.close()
