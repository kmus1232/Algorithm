from collections import defaultdict

"""
값을 저장하는 2차원 배열 : board
부모를 저장하는 2차원 배열 : parent
parent[r][c] == (r,c) -> merge되지 않았거나, 자신이 병합 셀의 부모(대표)인 경우 / 이때 board[r][c]의 값이 병합 셀의 대표 값
parent[r][c] != (r,c) -> 병합 셀의 일부인 경우 / 이때 board[r][c] 는 None 이거나, 값이 있더라도 의미가 없는 과거의 값이다

UPDATE r c value -> (r, c)의 부모 셀의 값을 바꾼다

UPDATE val1 val2 -> 모든 셀을 순회하면서 부모를 찾고, 부모의 값이 val1이면 val2로 바꾼다

MERGE r1 c1 r2 c2 -> (r1,c1) -> p1, (r2,c2) -> p2, 각각 부모를 찾는다.
이때 p1 == p2 면 무시한다.
p2만 값을 가지고 있는 경우만 p2 값을 사용한다. (p1만 갖거나 둘 다 값이 있는 경우는 그대로 p1 값 사용)
(r1,c1), (r2,c2) 중 좌표 순서상 앞의 셀을 부모로 삼고, 그 위치에 값을 저장한다.

UNMERGE r c -> 일단 (r,c)의 부모 p를 찾고, 모든 셀을 순회하면서 부모가 p인 셀들의 부모를 자신으로 설정하고 값도 None으로 설정한다.
(r,c)는 예외적으로 p의 값으로 설정한다.

PRINT r c -> (r,c) 부모 p 를 찾고 board[p]의 값을 출력한다

순회하면서 부모를 찾을 때 find_parent 함수는 부모 값도 업데이트 해준다.
부모를 업데이트 하는 기준은 좌표 순서
"""


def solution(commands):
    result = []  # PRINT 명령의 출력을 담을 배열

    board = []
    for r in range(51):
        row = []
        for c in range(51):
            row.append(None)
        board.append(row)

    parent = (
        []
    )  # (row, col) 을 담는 2차원 배열 [[(r1,c1), (r2,c2)], [(r3,c3), (r4,c4)]]
    for r in range(51):
        row = []
        for c in range(51):
            row.append((r, c))
        parent.append(row)

    def find_parent(r, c):
        pr, pc = parent[r][c]
        if (pr, pc) != (r, c):
            parent[r][c] = find_parent(pr, pc)
        return parent[r][c]

    def update(r, c, val):
        pr, pc = find_parent(r, c)
        board[pr][pc] = val

    def update_replace(val1, val2):
        for r in range(1, 51):
            for c in range(1, 51):
                pr, pc = find_parent(r, c)
                if board[pr][pc] == val1:
                    board[pr][pc] = val2

    def merge(r1, c1, r2, c2):
        pr1, pc1 = find_parent(r1, c1)
        pr2, pc2 = find_parent(r2, c2)
        if (pr1, pc2) == (pr2, pc2):
            return
        target_val = board[pr1][pc1] if board[pr1][pc1] else board[pr2][pc2]

        if not (pr1 < pr2 or (pr1 == pr2 and pc1 < pc2)):
            # 2번째 셀이 좌표 순서상 앞인 경우, 2번째 셀을 부모로 삼기 위해 좌표를 바꾼다
            pr1, pr2 = pr2, pr1
            pc1, pc2 = pc2, pc1
        parent[pr2][pc2] = (pr1, pc1)  # union
        board[pr1][pc1] = target_val

    def unmerge(r, c):
        pr, pc = find_parent(r, c)
        pval = board[pr][pc]
        replace_queue = []
        for i in range(1, 51):
            for j in range(1, 51):
                pi, pj = find_parent(i, j)
                if (pi, pj) == (pr, pc):
                    # 순회하면서 값을 변경할 경우 뒤의 셀들에 영향이 가기 때문에 큐에 담아두고 나중에 한번에 값을변경한다
                    replace_queue.append((i, j))

        for i, j in replace_queue:
            parent[i][j] = (i, j)
            board[i][j] = None if (i, j) != (r, c) else pval

    def _print(r, c):
        pr, pc = find_parent(r, c)
        result.append("EMPTY" if board[pr][pc] is None else board[pr][pc])

    for command in commands:
        command = command.split()
        com, arg = command[0], command[1:]
        if com == "UPDATE":
            if len(arg) == 3:
                r, c = map(int, arg[:2])
                val = arg[-1]
                update(r, c, val)
            else:
                val1, val2 = arg
                update_replace(val1, val2)
        elif com == "MERGE":
            r1, c1, r2, c2 = map(int, arg)
            merge(r1, c1, r2, c2)
        elif com == "UNMERGE":
            r, c = map(int, arg)
            unmerge(r, c)
        elif com == "PRINT":
            r, c = map(int, arg)
            _print(r, c)

    return result


print(
    solution(
        [
            "UPDATE 1 1 menu",
            "UPDATE 1 2 category",
            "UPDATE 2 1 bibimbap",
            "UPDATE 2 2 korean",
            "UPDATE 2 3 rice",
            "UPDATE 3 1 ramyeon",
            "UPDATE 3 2 korean",
            "UPDATE 3 3 noodle",
            "UPDATE 3 4 instant",
            "UPDATE 4 1 pasta",
            "UPDATE 4 2 italian",
            "UPDATE 4 3 noodle",
            "MERGE 1 2 1 3",
            "MERGE 1 3 1 4",
            "UPDATE korean hansik",
            "UPDATE 1 3 group",
            "UNMERGE 1 4",
            "PRINT 1 3",
            "PRINT 1 4",
        ]
    )
)
