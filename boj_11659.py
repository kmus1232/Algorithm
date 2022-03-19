import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.insert(0, 0)
for i in range(1, N + 1):
    nums[i] += nums[i-1]

for _ in range(M):
    i, j = map(int, input().split())
    print(nums[j] - nums[i-1])