#!/bin/python3

import math
import os
import random
import re
import sys

MAX_VAL = 200 + 1
count = [0] * MAX_VAL

def count_slice(s):
    # count occurences
    for i in s:
        count[i] += 1

def median_of_count(d):
    median = 0
    s = 0
    if d % 2 == 1:
        even = False
        stop = d // 2 
    else:
        even = True
        stop = d // 2 - 1
    
    for i in range(MAX_VAL):
        s += count[i]
            
        if s > stop:
            if even:
                median += i
                if stop == d // 2 - 1:
                    stop += 1
                else:
                    break                    
            else:
                median = 2 * i
                break
    return median

# Complete the activityNotifications function below.
def activityNotifications(expenditure, d):
    alerts = 0
    start = 0
    count_slice(expenditure[start: start + d])
    while start + d + 1 <= len(expenditure):
        # print(count)
        threshold = median_of_count(d)
        # print(expenditure[start + d], threshold)
        if expenditure[start + d] >= threshold:
            alerts += 1
        count[expenditure[start]] -= 1
        count[expenditure[start + d]] += 1
        start += 1
        
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
