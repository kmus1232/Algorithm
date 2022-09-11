from collections import deque

N, M = map(int, input().split())
dp = [100] * 101
q = deque()
warp_dict = dict()
for _ in range(N + M):
    a, b = map(int, input().split())
    warp_dict[a] = b

found_shortest_path = False
q.append((1, 0))
while q and not found_shortest_path:
    now, cost = q.popleft()
    for d in range(1, 7):
        nxt, next_cost = now + d, cost + 1
        if nxt > 100:
            break
        elif nxt == 100:
            found_shortest_path = True
            print(next_cost)
            break

        if dp[nxt] > next_cost:
            dp[nxt] = next_cost
            if nxt in warp_dict:
                warp = warp_dict[nxt]
                if dp[warp] > next_cost:
                    dp[warp] = next_cost
                    q.append((warp, next_cost))
            else:
                q.append((nxt, next_cost))
