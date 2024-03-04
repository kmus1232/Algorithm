import sys
sys.setrecursionlimit(5000)

def get_dist(r1, c1, r2, c2):
    return abs(r1 - r2) + abs(c1 - c2)

def solution(n, m, x, y, r, c, k):
    dist = get_dist(x, y, r, c)
    if dist > k or (k - dist) % 2:
        return "impossible"
    
    dir = [(1, 0, 'd'), (0, -1, 'l'), (0, 1, 'r'), (-1, 0, 'u')]
    
    def dfs(cr, cc, er, ec, path, k):
        if k == 0 and cr == er and cc == ec:
            return path
        
        for dr, dc, dchr in dir:
            nr, nc = cr + dr, cc + dc
            if 1 <= nr <= n and 1 <= nc <= m and get_dist(nr, nc, er, ec) <= k - 1:
                rst = dfs(nr, nc, er, ec, path + dchr, k - 1)
                if rst:
                    return rst
        return 
    
    return dfs(x, y, r, c, '', k)
