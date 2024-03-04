def solution(n, m, x, y, r, c, k):
    def find_dist(r1, c1, r2, c2):
        return abs(r1 - r2) + abs(c1 - c2)
    
    dist = find_dist(x, y, r, c)
    if dist > k or (k - dist) % 2:
        return "impossible"
    
    ans = ""
    
    for _ in range(k):
        if x + 1 <= n and find_dist(x + 1, y, r, c) <= k - 1:
            x += 1
            ans += "d"
        elif y - 1 >= 1 and find_dist(x, y - 1, r, c) <= k - 1:
            y -= 1
            ans += "l"
        elif y + 1 <= m and find_dist(x, y + 1, r, c) <= k - 1:
            y += 1
            ans += "r"
        else:
            x -= 1
            ans += "u"
        k -= 1
    
    return ans
