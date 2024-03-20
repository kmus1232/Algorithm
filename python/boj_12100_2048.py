UP = 1
DOWN = 2
RIGHT = 3
LEFT = 4


def move(cmd, board):
    def add_stack(board, stack, r, c):
        if board[r][c] == 0:
            return
        if stack and stack[-1][0] == board[r][c] and stack[-1][1] == False:
            stack.pop()
            stack.append((board[r][c] * 2, True))
        else:
            stack.append((board[r][c], False))

    n = len(board)
    new_board = [[0] * n for _ in range(n)]
    if cmd == UP:
        for c in range(n):
            stack = []  # (값: int, 이미 합쳐진 값인지 여부: bool)을 저장
            for r in range(n):
                add_stack(board, stack, r, c)
            for r, (val, _) in enumerate(stack):
                new_board[r][c] = val
    elif cmd == DOWN:
        for c in range(n):
            stack = []
            for r in range(n - 1, -1, -1):
                add_stack(board, stack, r, c)
            for r, (val, _) in enumerate(stack):
                new_board[n - 1 - r][c] = val
    elif cmd == LEFT:
        for r in range(n):
            stack = []
            for c in range(n):
                add_stack(board, stack, r, c)
            for c, (val, _) in enumerate(stack):
                new_board[r][c] = val
    elif cmd == RIGHT:
        for r in range(n):
            stack = []
            for c in range(n - 1, -1, -1):
                add_stack(board, stack, r, c)
            for c, (val, _) in enumerate(stack):
                new_board[r][n - 1 - c] = val

    return new_board


def dfs(cmd, board, count):
    new_board = move(cmd, board)

    if count == 5:
        return max([max(row) for row in new_board])
    return max(
        dfs(UP, new_board, count + 1),
        dfs(DOWN, new_board, count + 1),
        dfs(LEFT, new_board, count + 1),
        dfs(RIGHT, new_board, count + 1),
    )


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]


print(
    max(
        dfs(UP, board, 1),
        dfs(DOWN, board, 1),
        dfs(LEFT, board, 1),
        dfs(RIGHT, board, 1),
    )
)
