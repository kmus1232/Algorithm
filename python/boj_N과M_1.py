from typing import List

n, limit_count = map(int, input().split())

nums = [i + 1 for i in range(n)]

def permutations(nums, limit_count) -> List[List[int]]:
    result = []
    visit = [False] * len(nums)

    def go(arr, count):
        if count == limit_count:
            result.append(arr)
            return

        for i in range(len(nums)):
            if visit[i]:
                continue

            visit[i] = True
            go(arr + [nums[i]], count + 1)
            visit[i] = False


    go([], 0)

    return result

for e in permutations(nums, limit_count):
    print(*e)
