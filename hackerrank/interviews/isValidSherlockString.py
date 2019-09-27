#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

def letter_frequency(string):
    SHIFT = ord('a')
    freq = [0] * 30
    for letter in string:
        freq[ord(letter) - SHIFT] += 1
    return freq

# Complete the isValid function below.
def isValidSherlockString(s):
    freq = letter_frequency(s)
    count_freq = Counter(freq)
    count_freq.pop(0)
    if len(count_freq) > 2:
        return 'NO'
    elif len(count_freq) < 2:
        return 'YES'
    else:
        k1, v1 = count_freq.popitem()
        k2, v2 = count_freq.popitem()
        if abs(k1 - k2) == 1 and (v1 == 1 or v2 == 1) or k1 * v1 == 1 or k2 * v2 == 1:
            return 'YES'
        else:
            return 'NO'

if __name__ == '__main__':
    test7 = 'ibfdgaeadiaefgbhbdghhhbgdfgeiccbiehhfcggchgghadhdhagfbahhddgghbdehidbibaeaagaeeigffcebfbaieggabcfbiiedcabfihchdfabifahcbhagccbdfifhghcadfiadeeaheeddddiecaicbgigccageicehfdhdgafaddhffadigfhhcaedcedecafeacbdacgfgfeeibgaiffdehigebhhehiaahfidibccdcdagifgaihacihadecgifihbebffebdfbchbgigeccahgihbcbcaggebaaafgfedbfgagfediddghdgbgehhhifhgcedechahidcbchebheihaadbbbiaiccededchdagfhccfdefigfibifabeiaccghcegfbcghaefifbachebaacbhbfgfddeceababbacgffbagidebeadfihaefefegbghgddbbgddeehgfbhafbccidebgehifafgbghafacgfdccgifdcbbbidfifhdaibgigebigaedeaaiadegfefbhacgddhchgcbgcaeaieiegiffchbgbebgbehbbfcebciiagacaiechdigbgbghefcahgbhfibhedaeeiffebdiabcifgccdefabccdghehfibfiifdaicfedagahhdcbhbicdgibgcedieihcichadgchgbdcdagaihebbabhibcihicadgadfcihdheefbhffiageddhgahaidfdhhdbgciiaciegchiiebfbcbhaeagccfhbfhaddagnfieihghfbaggiffbbfbecgaiiidccdceadbbdfgigibgcgchafccdchgifdeieicbaididhfcfdedbhaadedfageigfdehgcdaecaebebebfcieaecfagfdieaefdiedbcadchabhebgehiidfcgahcdhcdhgchhiiheffiifeegcfdgbdeffhgeghdfhbfbifgidcafbfcd'
    result = isValidSherlockString(test7)
    assert(result == 'YES')
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValidSherlockString(s)

    fptr.write(result + '\n')

    fptr.close()
