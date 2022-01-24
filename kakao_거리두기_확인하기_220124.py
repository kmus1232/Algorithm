def isPlacePartitioned(place) -> int:
    for x in range(5):
        for y in range(5):
            if place[x][y] != 'P':
                continue
            else:
                if isPeoplePartitioned(x, y, place):
                    continue
                else:
                    return 0
    return 1


def isPeoplePartitioned(x, y, place) -> bool:
    from collections import deque
    q = deque()
    q.append((x, y))
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[x][y] = True
    dx = [1, 0, -1, 0]
    dy = [0, -1, 0, 1]

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if not (0 <= nx < 5) or not (0 <= ny < 5) \
                    or visited[nx][ny] or place[nx][ny] == "X" \
                    or (abs(nx - x) + abs(ny - y)) > 2:
                continue
            elif place[nx][ny] == "P":
                return False
            else:
                q.append((nx, ny))
                visited[nx][ny] = True
    return True


def solution(places):
    result = []
    for place in places:
        result.append(isPlacePartitioned(place))

    return result
