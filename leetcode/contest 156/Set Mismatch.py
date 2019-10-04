from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n = len(nums)
        progression_sum = (n + 1) * n // 2
        curr_sum = sum(nums)
        c = Counter(nums)
        for k, v in c.items():
            if v > 1:
                orig = progression_sum - curr_sum + k
                return [k, orig]
        