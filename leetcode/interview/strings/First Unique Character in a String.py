# First Unique Character in a String

# Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

# Examples:

# s = "leetcode"
# return 0.

# s = "loveleetcode"
# return 2.
 

# Note: You may assume the string contains only lowercase English letters.


# You are here!
# Your runtime beats 87.94 % of python3 submissions.
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i, l in enumerate(s):
            if s.find(l, i+1) == -1 and s.rfind(l, 0, i) == -1:
                return i
        return -1