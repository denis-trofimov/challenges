#!/bin/python3

import math
import os
import random
import re
import sys


def all_substrings(s):
    n = len(s)
    for l in range(1, n):
        i = 0
        substrings = []
        while i <= n - l:
            substrings.append(s[i: i + l])
            i += 1
        yield (substrings)

def is_palindrome(s):
    n = len(s)
    if n == 1:
        return True
    elif not n:
        return False
    base = s[0]
    for i in range(n // 2):
        if s[i] != base or s[n -1 - i] != base:
            return False
    return True


# Complete the substrCount function below.
def substrCount(n, s):
    count = 0
    for substring_list in all_substrings(s):
        for substring in substring_list:
            if is_palindrome(substring):
                count += 1
    if is_palindrome(s):
                count += 1
    return count

if __name__ == '__main__':
    assert(substrCount(5, 'asasd') == 7)
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = substrCount(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
