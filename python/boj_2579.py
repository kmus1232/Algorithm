n = int(input())

stairs = []
for _ in range(n):
    stairs.append(int(input()))


def solution(arr):
    if len(arr) <= 2:
        return sum(arr)

    table = [[0, 0] for _ in range(n)]
    table[0][0], table[0][1] = arr[0], arr[0]
    table[1][0], table[1][1] = arr[1], arr[0] + arr[1]

    for i in range(2, n):
        table[i][0] = max(table[i - 2]) + arr[i]
        table[i][1] = table[i - 1][0] + arr[i]

    return max(table[n - 1])


print(solution(stairs))
