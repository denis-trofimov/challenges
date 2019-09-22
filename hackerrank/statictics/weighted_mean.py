# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = list(map(int, input().rstrip().split()))
w = list(map(int, input().rstrip().split()))

divident = sum(map(lambda x, y: x * y, x, w))
divizor = sum(w)
weighted_mean = float(divident) / divizor
print(f"{weighted_mean:.1f}")