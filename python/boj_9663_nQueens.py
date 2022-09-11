N = int(input())
count = 0
location = [0] * N


def is_promising(r):
    for i in range(r):
        if location[i] == location[r] or abs(location[i] - location[r]) == r - i:
            return False
    return True


def dfs(r):
    if r == N:
        global count
        count += 1
        return

    for c in range(N):
        location[r] = c
        if is_promising(r):
            dfs(r + 1)


dfs(0)
print(count)
