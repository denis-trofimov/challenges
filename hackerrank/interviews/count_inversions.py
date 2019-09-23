#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the coun_inversions function below.

def merge_count_inversions(len_left, left, len_right, right):
    split_inversions = i = j = 0
    sorted_list = []
    while i < len_left and j < len_right:
        l = left[i]
        r = right[j]
        if l <= r:
            sorted_list.append(l)
            i += 1
        else:
            sorted_list.append(r)
            j += 1
            split_inversions += len_left - i
    while i < len_left:
        sorted_list.append(left[i])
        i += 1
    while j < len_right:
        sorted_list.append(right[j])
        j += 1            

    return split_inversions, sorted_list

def merge_sort_count_inversions(n: int, arr: list):
    if n == 1:
        return 0, arr
    left_inversions , left_half  = merge_sort_count_inversions(n // 2, arr[:n // 2])
    right_inversions, right_half = merge_sort_count_inversions(n - n // 2, arr[n // 2:])
    split_inversions, sorted_list = merge_count_inversions(n // 2, left_half, n - n // 2, right_half)
    inversions = left_inversions + right_inversions + split_inversions
    return inversions, sorted_list

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        n = int(input())

        arr = list(map(int, input().rstrip().split()))

        result, _ = merge_sort_count_inversions(n, arr)

        fptr.write(str(result) + '\n')

    fptr.close()

def test():
    n = 5  
    arr = list(map(int, '1 1 1 2 2'.rstrip().split()))
    result, sorted_list = merge_sort_count_inversions(n, arr)
    assert(result == 0) 
    n = 5  
    arr = list(map(int, '2 1 3 1 2'.rstrip().split()))
    result, sorted_list = merge_sort_count_inversions(n, arr)
    assert(result == 4) 
    