#!/usr/bin/env python3
"""Picture downloader."""
import requests
from functools import wraps
from time import time
from tempfile import TemporaryFile


def timing(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        te = time()
        if 'log_time' in kw:
            name = kw.get('log_name', f.__name__.upper())
            kw['log_time'][name] = int((te - ts) * 1000)
        else:
            print(f'func: {f.__name__} took: {te-ts:2.4f} sec')
        return result
    return wrap


def get_file(url):
    r = requests.get(url, allow_redirects=True)
    r.raise_for_status()
    # if r.status_code != 200:
    #     return None
    return r

def write_file(response):
    # https://loremflickr.com/cache/resized/65535_48642791151_6c5abf5583_320_240_nofilter.jpg
    # name = response.url.split('/')[-1]
    # with open(name, 'wb') as file:
    with TemporaryFile() as file:
        file.write(response.content)

@timing
def main():
    url = "https://loremflickr.com/320/240"
    for _ in range(10):
        write_file(get_file(url))

if __name__ == "__main__":
    main()
