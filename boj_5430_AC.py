from collections import deque


def solution(cmds: str, data: deque):
    is_reverse = False
    for cmd in cmds:
        if cmd == 'R':
            is_reverse = not is_reverse
        else:
            if not data:
                print('error')
                return
            else:
                if is_reverse:
                    data.pop()
                else:
                    data.popleft()

    if is_reverse:
        data = list(data)[::-1]
    print('[' + ','.join(data) + ']')


n = int(input())

for _ in range(n):
    cmds = input()
    _ = input()
    data = input()
    if data == '[]':
        data = deque()
    else:
        data = deque(data.strip('[]').split(','))

    solution(cmds, data)
