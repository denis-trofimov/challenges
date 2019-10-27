import math


def is_prime(num):
    if num == 1:
        return False
    if not num % 2 and num != 2:
        return False
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if not num % i:
            return False
    return True


class Solution:
    def countPrimes(self, n: int) -> int:
        total = 1
        for i in range(3, n, 2):
            if is_prime(i):
                total += 1
        return total
    

if __name__ == "__main__":
    assert is_prime(1) == False
    assert is_prime(2) == True
    assert is_prime(3) == True
    assert is_prime(17) == True
    assert is_prime(9) == False