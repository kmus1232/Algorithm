class Node:
    def __init__(self, idx):
        self.idx = idx
        self.up = None
        self.down = None
        self.in_list = True

def solution(n, k, cmd):
    node_arr = [Node(i) for i in range(n)]
    for i in range(n):
        if i > 0:
            node_arr[i].up = node_arr[i - 1]
        if i < n - 1:
            node_arr[i].down = node_arr[i + 1]

    curr = node_arr[k]
    stack = []

    for c in cmd:
        if len(c) > 1:
            c, n = c.split()
            n = int(n)
            if c == 'U':
                for _ in range(n):
                    curr = curr.up
            else:
                for _ in range(n):
                    curr = curr.down
        else:
            if c == 'C':
                curr.in_list = False
                stack.append(curr)
                up = curr.up
                down = curr.down
                if up:
                    up.down = down
                if down:
                    down.up = up
                    curr = down
                else:
                    curr = up
            else:
                restore = stack.pop()
                restore.in_list = True
                up = restore.up
                down = restore.down
                if up:
                    up.down = restore
                if down:
                    down.up = restore
    
    ans = ''
    for node in node_arr:
        if node.in_list:
            ans += 'O'
        else:
            ans += 'X'
    
    return ans