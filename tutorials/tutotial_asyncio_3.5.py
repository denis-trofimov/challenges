#!/usr/bin/env python3
"""Back to python 3.5 asyncio"""
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
    task1 = asyncio.ensure_future(print_nums())
    task2 = asyncio.ensure_future(print_time())
    await asyncio.gather(task1, task2)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
