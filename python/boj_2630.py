n = int(input())
board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

def determine_color(board, x, y, l):
    flag = True
    color = board[x][y]
    for i in range(x, x + l):
        for j in range(y, y + l):
            if board[i][j] != color:
                flag = False
        if not flag:
            break
    
    if flag:
        return (1, 0) if board[x][y] == 0 else (0, 1)
    else:
        l //= 2
        white = blue = 0
        diff = [(0,0), (0,l), (l,0), (l,l)]
        for dx, dy in diff:
            rst = determine_color(board, x + dx, y + dy, l)
            white += rst[0]
            blue += rst[1]
        return (white, blue)


white, blue = determine_color(board, 0, 0, len(board))
print(white, blue, sep='\n')