#!/bin/python3

import math
import os
import random
import re
import sys


from collections import Counter


# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    def is_anagramm(freq1, freq2):
        for k, v in freq1.items():
            opposite = freq2.get(k)
            if v != opposite:
                return False
        return True
        

    def all_substrings(str: s):
        n = len(s)
        for l in range(1, n):
            i = 0
            possible_anagrams = []
            while i <= n - l:
                possible_anagrams.append(s[i: i + l])
                i += 1
            yield (possible_anagrams)

    anagrams = 0    
    for possible_anagrams in all_substrings(s):
        list_freq = []
        for word in (possible_anagrams):
            list_freq.append(Counter(word))

        for i, freq in enumerate(list_freq):
            for j in range(i + 1, len(possible_anagrams)):
                freq2 = list_freq[j]
                if is_anagramm(freq, freq2):
                    anagrams += 1
    return anagrams
            


if __name__ == '__main__':
    # inline tests
    res = sherlockAndAnagrams('abba')
    assert(res == 4)
    assert(sherlockAndAnagrams('abcd') == 0)
    assert(sherlockAndAnagrams('ifailuhkqq') == 3)
    assert(sherlockAndAnagrams('kkkk') == 10)
    assert(sherlockAndAnagrams('cdcd') == 5)

    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
