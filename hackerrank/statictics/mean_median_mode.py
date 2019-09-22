# Day 0: Mean, Median, and Mode
# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
x = list(map(int, input().rstrip().split()))

mean = float(sum(x)) / n
print(f"{mean:.1f}")


from collections import Counter
freq = Counter(sorted(x))

def median_freq(freq, n):
    median = 0.0
    if not n % 2:
        stop = n // 2 - 1
    else:
        stop = n // 2
    s = 0
    for k, v in freq.items():
        s += v
        if s > stop:
            if n % 2:
                median = k
                break
            elif not median:
                stop += 1
                if s > stop:
                    median = k
                else:
                    median += k / 2
            else:
                median += k / 2
                break
    return median

median = median_freq(freq, n)
print(f"{median:.1f}")


mode = freq.most_common(1)[0][0]
print(mode)
