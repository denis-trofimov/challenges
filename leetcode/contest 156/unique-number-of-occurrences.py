from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        c = Counter(arr)
        l = list(c.values())
        c2 = Counter(l)
        for i in c2.values():
            if i > 1:
                return False
        return True