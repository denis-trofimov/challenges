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
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    # Write your code here.

n = int(input())
print(fibonacci(n))

