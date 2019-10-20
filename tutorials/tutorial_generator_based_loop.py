#!/usr/bin/env python3
"""Generator based loop. tutorial video 9."""
from time import time, sleep
from collections import deque


def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        yield

def print_time():
    count = 0
    while True:
        if not count % 3:
            print('bang')
        count += 1
        yield

queue = deque((print_nums(), print_time()))
def main():
    while True:
        gen = queue.popleft()
        next(gen)
        queue.append(gen)
        sleep(.2)


if __name__ == "__main__":
    main()
