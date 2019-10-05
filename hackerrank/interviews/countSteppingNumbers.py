from math import log10
from typing import List, Tuple, Dict, TextIO

# def check(n):
#     digits = [int(s) for s in str(n)]
#     # print(digits)
#     prev = digits.pop()
#     while digits:
#         curr = digits.pop()
#         if abs(curr - prev) != 1:
#             # print(prev, curr)
#             return False
#         prev = curr
#     return True

def memoization(func):
    cache = {}

    def wrapper(*args):
        value = cache.get(args)
        if not value:
            value = func(*args)
            cache[args] = value
        return value

    return wrapper

@memoization
def stepping(order):
    if order == 1:
        return [i for i in range(10)]
    res = []
    prev = stepping(order - 1)
    for n in prev:
        d = n % 10
        if d > 0:
            res.append(10 * n + d - 1)
        if d < 9 and n:
            res.append(10 * n + d + 1)
    return res
    
class Solution: 
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        res = []
        # for i in range(low, high + 1):
        #     if check(i):
        #         res.append(i)
        
        for order in range(1 if low < 10 else int(log10(low)), int(log10(high + 1)) + 2):
            print(order)
            sn = stepping(order)
            for n in sn:
                if n >= low and n <= high:
                    res.append(n)
        return res
    
if __name__ == "__main__":
    sol = Solution()
    res = sol.countSteppingNumbers(0, 21)
    assert res == [0,1,2,3,4,5,6,7,8,9,10,12,21]