# You are here!
# Your runtime beats 16.87 % of python3 submissions.
# You are here!
# Your memory usage beats 43.86 % of python3 submissions.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def common_prefix(s1, s2):
            l = min(len(s1), len(s2))
            for i in range(l):
                if s1[i] != s2[i]:
                    return s1[:i]
            return s1[:l]
        
        prefix = strs[0]
        if len(strs) == 1:
            return prefix
        
        for some in strs[1:]:
            prefix = common_prefix(prefix, some)
            if prefix == "":
                break
        
        return prefix
