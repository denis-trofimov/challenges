# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

# Follow up:
# What if the inputs contain unicode characters? How would you adapt your solution to such case?
# You are here!
# Your runtime beats 85.92 % of python3 submissions.

from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        if n != len(t):
            return False        
        counter_s = Counter(s)
        counter_t = Counter(t)
        for k, v in counter_s.items():
            if counter_t[k] != v:
                return False
        return True
            