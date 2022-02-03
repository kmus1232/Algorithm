from collections import deque

def time_to_int(time: str) -> int:
    h, m = map(int, time.split(":"))
    return h * 60 + m

def solution(n, t, m, timetable):
    people_queue = deque(sorted(map(time_to_int, timetable)))
    bus_queue = deque([540 + t * i for i in range(n)])

    ans = 0
    for bus in bus_queue:
        cnt = 0
        last_passenger = None
        while people_queue and people_queue[0] <= bus and cnt < m:
            last_passenger = people_queue.popleft()
            cnt += 1
        if cnt < m: # 기다리는 승객을 태우고도 자리가 남을 때
            ans = max(ans, bus)
        else: # 꽉 차서 일찍 와야할 때
            ans = max(ans, last_passenger - 1)

    h, m = ans // 60, ans % 60
    return str(h).zfill(2) + ":" + str(m).zfill(2)
