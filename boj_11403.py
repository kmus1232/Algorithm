N = int(input())

board = []
for _ in range(N):
    board.append(list(map(int, input().split())))

for c in range(N):
    for a in range(N):
        for b in range(N):
            if board[a][c] == 1 and board[c][b] == 1:
                board[a][b] = 1

for row in board:
    print(*row)