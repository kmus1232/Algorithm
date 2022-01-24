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
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[x][y] = True
    arr_dx = [1, 0, -1, 0]
    arr_dy = [0, -1, 0, 1]

    def bfs(dx, dy):
        if not (0 <= x + dx < 5) or not (0 <= y + dy < 5):
            return True
        if visited[x + dx][y + dy] or (abs(dx) + abs(dy)) > 2:
            return True

        visited[x + dx][y + dy] = True
        if place[x + dx][y + dy] == "X":
            return True
        elif place[x + dx][y + dy] == "P":
            return False
        else:
            for i in range(4):
                if not bfs(dx + arr_dx[i], dy + arr_dy[i]):
                    return False
        return True

    for i in range(4):
        if not bfs(arr_dx[i], arr_dy[i]):
            return False
    return True


def solution(places):
    result = []
    for place in places:
        result.append(isPlacePartitioned(place))

    return result
