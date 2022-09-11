def solution(lines):
    start_end_list = []
    for data in lines:
        _, end_time, cost = data.split()
        h, m, s = end_time.split(':')
        end_time = (3600 * int(h) + 60 * int(m)) * 1000 \
            + int(s.replace('.', ''))
        cost = cost[:-1]
        if cost.isdecimal():
            cost = int(cost) * 1000
        else:
            cost = int(cost.ljust(5, '0').replace('.', ''))
        start_time = end_time - cost + 1
        start_end_list.append([start_time, end_time])

    max_count = 1
    for i in range(len(start_end_list)):
        s, e = start_end_list[i]
        p = e + 999
        count = 1
        for j in range(i + 1, len(start_end_list)):
            cmp_s = start_end_list[j][0]
            if cmp_s <= p:
                count += 1
        max_count = max(max_count, count)

    return max_count
