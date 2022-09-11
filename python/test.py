print("강의실 배정 프로그램을 시작합니다.")
print("가능한 많은 예약을 받기 위해 취소되는 예약이 생길 수 있습니다.\n")

q = []
while True:
    print("예약하고자 하는 시간을 입력해주세요")
    print("시작 시간 : ", end='')
    start = int(input())
    print("종료 시간 : ", end='')
    end = int(input())

    if start >= end:
        print("잘못된 입력입니다.")
        continue

    q.append((start, end))

    print("예약 입력을 계속 하시겠습니까? (Y/N) : ", end='')
    select = input()
    if select in {'N', 'n'}:
        break

q.sort(key=lambda a: (a[1], a[0]), reverse=True)  # 끝나는 시간 순으로 오름차순 정렬
result = [q.pop()]
while q:
    if q[-1][0] >= result[-1][1]:
        result.append(q.pop())
    else:
        q.pop()

print("\n확정된 예약 시간표입니다.")
print(result)
