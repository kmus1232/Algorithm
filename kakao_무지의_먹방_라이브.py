from heapq import *


def solution(food_times, k):
    if sum(food_times) <= k:
        return -1

    heap = [(food, i + 1) for i, food in enumerate(food_times)]
    heapify(heap)
    rest = len(food_times)
    prev_s = 0

    while True:
        s = heap[0][0]
        if (s - prev_s) * rest <= k:
            k -= (s - prev_s) * rest
            prev_s = s
            while heap and heap[0][0] == s:
                heappop(heap)
                rest -= 1
        else:
            k %= rest
            return sorted(heap, key=lambda x: x[1])[k][1]
