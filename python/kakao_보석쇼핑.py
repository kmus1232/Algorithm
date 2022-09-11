def solution(gems):
    gems_set = set(gems)
    gems_count_dict = {gem: 0 for gem in gems_set}  # 투 포인터 범위 안의 보석들을 카운트
    i, j = 0, -1
    ans = [i, j]
    ans_range = len(gems)
    count_collected_gem = 0

    while j < len(gems) - 1:
        j += 1  # 없는 보석이 있으므로 범위를 늘려가며 탐색한다
        gems_count_dict[gems[j]] += 1
        if gems_count_dict[gems[j]] == 1:
            count_collected_gem += 1

        while count_collected_gem == len(gems_set):  # 보석을 모두 갖고있는 동안 계속 반복
            if j - i < ans_range:
                ans = [i + 1, j + 1]
                ans_range = j - i
            i += 1  # 왼쪽 포인터를 앞으로 이동시켜 범위를 좁힌다
            gems_count_dict[gems[i - 1]] -= 1
            if gems_count_dict[gems[i - 1]] == 0:
                count_collected_gem -= 1

    return ans