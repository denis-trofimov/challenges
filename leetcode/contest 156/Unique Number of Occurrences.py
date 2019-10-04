from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        c = Counter(arr)
        l = list(c.values())
        c2 = Counter(l)
        for i in c2.values():
            if i > 1:
                return False
        return True

if __name__ == "__main__":
    sol = Solution()
    case_input = [1,2]
    answer = sol.uniqueOccurrences(case_input)
    print(answer)
    expected = False
    assert expected == answer