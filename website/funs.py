import os
import time, sys
from functools import lru_cache

print(os.getcwd())


def nextFib(number=0):
    ctr = 0
    while number > (currFib := fib(ctr)):
        ctr += 1
    return currFib


@lru_cache(maxsize=100)
def fib(n):
    return n if n <= 0 or n == 1 else fib(n - 1) + fib(n - 2)

# print(sys.getrecursionlimit())
# sys.setrecursionlimit(2000)
# start_time = time.time()
# nextFib(566 + 64 + 26 + 26742687425687256)
# execTime = (time.time() - start_time) * 1000
# print("Part %.5s ms\n" % execTime)
# sys.setrecursionlimit(1000)
