import math


n = int(input())
x = list(map(float, input().rstrip().split()))

mean = float(sum(x)) / n
squared_distance = map(lambda x: (x - mean) ** 2, x)
standard_deviation = math.sqrt(sum(squared_distance) / n)
print(f'{standard_deviation:.1f}')