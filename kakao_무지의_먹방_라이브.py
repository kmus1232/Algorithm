from heapq import *


def solution(food_times, k):
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
            if k == 0:
                if not heap:
                    return -1
                else:
                    return sorted(heap, key=lambda x: x[1])[0][1]
        else:
            k %= rest
            return sorted(heap, key=lambda x: x[1])[k][1]


print(solution([4,5,2,8], 10))
print(solution([1, 5, 5, 5, 5, 6, 7], 31))