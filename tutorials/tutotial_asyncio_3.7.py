#!/usr/bin/env python3
"""Back to python 3.7 asyncio"""
from time import time
import asyncio


async def print_nums():
    num = 1
    while True:
        print(num)
        num += 1
        await asyncio.sleep(1)

async def print_time():
    count = 0
    while True:
        if not count % 3:
            print(f'{count} seconds have passed')
        count += 1
        await asyncio.sleep(1)

async def main():
    task1 = asyncio.create_task(print_nums())
    task2 = asyncio.create_task(print_time())
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    asyncio.run(main())
