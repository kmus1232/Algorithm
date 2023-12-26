# 작은 풍선은 최대 1번 터트릴 수 있고, 큰 풍선은 무제한으로 터트릴 수 있음
# 기회는 아끼는게 좋음
# dp_left[i][0] -> i번째 풍선의 왼쪽 풍선들 중에서 살릴 수 있는 가장 큰 풍선 + 0 ~ i-1 풍선을 터트릴 때 작은 풍선을 한번도 안터트림
# dp_left[i][1] -> 작은 풍선을 터트림
# dp_left, dp_right 를 미리 계산 한다.
# dp 배열은, 가능한 한 큰 값을 남겨야 한다.
# i 번째 풍선을 살릴 수 있느냐 -> 아래 3가지 케이스를 살펴서 하나라도 참이라면 살릴 수 있음
# 1. dp_left[i][0], dp_right[i][0] -> 풍선 i 보다 값이 큰게 하나라도 있다면 ok, 찬스를 안썼기 때문에 작은거 하나 있더라도 가능함
# 2. dp_left[i][1], dp_right[i][0]
# 3. dp_left[i][0], dp_right[i][1]
# 2, 3번의 경우에는 두 값이 전부 i번째 풍선보다 크거나 같아야 함 (같은 경우는 양쪽 맨 끝의 경우를 위해)

# dp_left[i][0] -> 찬스를 계속 쓰지 않아야 함 - 선택권이 없음
# dp_left[i][0] = min(dp_left[i-1][0], a[i])

# dp_left[i][1] -> 찬스 안쓴 상태에서 찬스를 쓰거나, 찬스 쓴 값을 가져가거나 - 둘 중 큰 값을 선택함
# dp_left[i][1] = max( max(dp_left[i-1][0], a[i]), min(dp_left[i-1][1], a[i]) )

def solution(a):
    dp_left = [[None, None] for _ in range(len(a))]
    dp_left[0][0] = dp_left[0][1] = a[0]
    for i in range(1, len(a)):
        dp_left[i][0] = min(dp_left[i-1][0], a[i])
        dp_left[i][1] = max(max(dp_left[i-1][0], a[i]), min(dp_left[i-1][1], a[i]))

    dp_right = [[None, None] for _ in range(len(a))]
    dp_right[-1][0] = dp_right[-1][1] = a[-1]
    for i in range(len(a) - 2, -1, -1):
        dp_right[i][0] = min(dp_right[i+1][0], a[i])
        dp_right[i][1] = max(max(dp_right[i+1][0], a[i]), min(dp_right[i+1][1], a[i]))

    result = []
    for i in range(len(a)):
        cur = a[i]
        if (
            (cur <= dp_left[i][1] and cur <= dp_right[i][0]) or
            (cur <= dp_left[i][0] and cur <= dp_right[i][1]) or
            (cur <= dp_left[i][0] or cur <= dp_right[i][0])
        ):
            result.append(cur)

    return len(result)


solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]	)
