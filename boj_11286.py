from heapq import *
import sys
input = sys.stdin.readline

N = int(input())
heap = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if not heap:
            print(0)
        else:
            e, is_plus = heappop(heap)
            print(e if is_plus else -e)
    elif x < 0:
        heappush((-x, False))
    else:
        heappush((x, True))
