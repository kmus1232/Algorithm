N, K = map(int, input().split())
items = []
for i in range(N):
    weight, value = map(int, input().split())
    items.append((i, weight, value))

visited = [False] * N

def calc_ideal_value(i, avail_weight):
    sorted_items = sorted(items, key=lambda x: x[2]/x[1], reverse=True)
    ideal = 0
    for idx, w, v in sorted_items:
        if visited[idx] or idx < i:
            continue

        if avail_weight >= w:
            avail_weight -= w
            ideal += v
        else:
            ideal += (v / w) * avail_weight
            break

    return ideal

def solution():
    max_profit = 0
    def knapsack(i, avail_weight):
        if i >= N or avail_weight <= 0:
            return

        sum_weight = sum([items[i][1] for i in range(N) if visited[i]])
        sum_value = sum([items[i][2] for i in range(N) if visited[i]])

        _, weight, value = items[i]
        if weight <= avail_weight:
            B = calc_ideal_value(i + 1, avail_weight - weight)
            if max_profit < sum_value + value + B:
                visited[i] = True
