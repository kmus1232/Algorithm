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
    q.append((x, y, 0))
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[x][y] = True
    D = ((-1, 0), (1, 0), (0, -1), (0, 1))

    while q:
        cx, cy, cdst = q.popleft()
        for dx, dy in D:
            nx, ny, ndst = cx + dx, cy + dy, cdst + 1
            if not (0 <= nx < 5) or not (0 <= ny < 5) or ndst > 2 \
                    or visited[nx][ny] or place[nx][ny] == "X":
                continue
            elif place[nx][ny] == "P":
                return False
            else:  # place[nx][ny] == "O"
                q.append((nx, ny, ndst))
                visited[nx][ny] = True
    return True


def solution(places):
    result = []
    for place in places:
        result.append(isPlacePartitioned(place))

    return result
