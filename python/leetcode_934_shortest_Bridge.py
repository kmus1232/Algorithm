from collections import deque
from typing import List


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)
        direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visit = set()
        
        def invalid(r, c):
            return r < 0 or r == N or c < 0 or c ==N
        
        # visit에 섬을 기록한다.
        def dfs(r, c):
            if invalid(r, c) or not grid[r][c] or (r, c) in visit:
                return
            visit.add((r, c))
            for dr, dc in direct:
                dfs(r + dr, c + dc)
        
        # 섬 둘레를 한 칸씩 확장한다.
        def bfs():
            q = deque(visit)
            ans = 0
            while q:
                length = len(q)
                for _ in range(length):
                    r, c = q.popleft()
                    for dr, dc in direct:
                        nr, nc = r + dr, c + dc
                        if invalid(nr, nc) or (nr, nc) in visit:
                            continue
                        if grid[nr][nc] == 1:
                            return ans
                        visit.add((nr, nc))
                        q.appen((nr, nc))
                ans += 1
                
        
        for r in range(N):
            for c in range(N):
                if grid[r][c] == 1:
                    dfs(r, c)
                    return bfs()


if __name__ == "__main__":
    sol = Solution()
    print(sol.shortestBridge([[1, 1, 0, 1, 0, 0, 1, 1, 0, 0], [0, 1, 1, 1, 1, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 1, 1, 0, 0], [0, 0, 0, 1, 0, 0, 1, 0, 1, 0], [
          0, 0, 0, 0, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 1, 1, 1, 0, 1, 0], [0, 0, 0, 0, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 1, 0, 0, 0]]))
