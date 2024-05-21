# You are here!
# Your runtime beats 64.37 % of python3 submissions.
# https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/884/

class Solution:
    def myAtoi(self, s: str) -> int:
        def read_sign(s):
            length = len(s)
            for i, l in enumerate(s):
                if l == "-":
                    if i == length-1:
                        return l, ""
                    return l, s[i+1:]
                elif l == "+":
                    if i == length-1:
                        return "", ""
                    return "", s[i+1:]
                else:
                    return "", s
                    
        stripped = s.strip()
        if stripped == "":
            return 0
                    
        sign, left = read_sign(stripped)
        valid = ""
        for l in left:
            if l.isnumeric():
                valid = valid + l
            else:
                break
                
        if valid == "":
            return 0
        
        number = float(sign + valid)
        if number > 2147483647:
            return 2147483647
        elif number < -2147483648:
            return -2147483648
        return int(number)
