from collections import defaultdict

IN = 0
OUT = 1

def solution(edges):
    nodes = defaultdict(lambda: {IN: 0, OUT: 0})
    for s, e in edges:
        nodes[s][OUT] += 1
        nodes[e][IN] += 1

    # 생성한 정점(루트) = in == 0 and out >= 2
    # 막대 그래프 개수 = out == 0
    # 8자 그래프 개수 = out == 2 and (in == 2 or in == 3)
    # 도넛 그래프 개수 = root_out - bar - eight

    root = None
    total_cnt = 0
    bar_cnt = 0
    eight_cnt = 0

    for node, info in nodes.items():
        if info[IN] == 0 and info[OUT] >= 2:
            root = node
            total_cnt = info[OUT]
        elif info[OUT] == 0:
            bar_cnt += 1
        elif info[OUT] == 2 and (info[IN] == 2 or info[IN] == 3):
            eight_cnt += 1

    donut_cnt = total_cnt - bar_cnt - eight_cnt

    return [root, donut_cnt, bar_cnt, eight_cnt]
