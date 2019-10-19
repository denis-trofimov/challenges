#!/usr/bin/env python3
"""Picture downloader.

Tutorial video https://youtu.be/LO61F07s7gw
"""

import aiohttp
import asyncio
from time import time
from tempfile import TemporaryFile
# import aiofiles


def write_file(data):
    with TemporaryFile() as file:
        file.write(data)

# async def aio_write(data):
#     name = f'file-{int(time() * 1000000)}.jpeg'
#     async with aiofiles.open(name, 'wb') as f:
#         await f.write(data)

async def fetch(session, url):
    async with session.get(url, allow_redirects=True) as response:
        data = await response.read()
        # await aio_write(data)
        write_file(data)

async def main():
    url = "https://loremflickr.com/320/240"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for _ in range(10):
            task = asyncio.create_task(fetch(session, url))
            tasks.append(task)

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    ts = time()
    asyncio.run(main())
    print(f'took: {time()-ts:2.4f} sec')
