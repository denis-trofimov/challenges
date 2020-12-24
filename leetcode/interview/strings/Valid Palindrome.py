# You are here!
# Your runtime beats 76.88 % of python3 submissions.

# Valid Palindrome

# Solution
# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

# Note: For the purpose of this problem, we define empty string as valid palindrome.

# Example 1:

# Input: "A man, a plan, a canal: Panama"
# Output: true
# Example 2:

# Input: "race a car"
# Output: false
 

# Constraints:

# s consists only of printable ASCII characters.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = [l for l in s.lower() if l.isalnum()]
        n = len(alphanumeric) - 1
        for i, l in enumerate(alphanumeric):
            if l != alphanumeric[n - i]:
                return False
        return True