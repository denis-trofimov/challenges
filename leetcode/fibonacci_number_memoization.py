def memoization(func):
    cache = {}

    def wrapper(*args):
        value = cache.get(args)
        if not value:
            value = func(*args)
            cache[args] = value
        return value

    return wrapper

class Solution(object):
    
    # Write your code here.
    @memoization
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
