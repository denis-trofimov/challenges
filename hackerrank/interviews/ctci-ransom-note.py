#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    def fill_dict(magazine):
        m_dict = {}
        for key in magazine:
            value = m_dict.get(key)
            if not value:
                m_dict[key] = 1
            else:
                m_dict[key] = value + 1
        return m_dict

    answer = "Yes"
    m_dict = fill_dict(magazine)

    for word in note:
        qty = m_dict.get(word)
        if not qty:
            answer = "No"
            break
        else:
            if qty > 1:
                m_dict[word] = qty - 1
            else:
                m_dict.pop(word)
    print(answer)
    return answer


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
