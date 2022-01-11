def solution(s):
    ans = len(s)
    for l in range(1, len(s) // 2 + 1):
        words = [s[i: i + l] for i in range(0, len(s), l)]
        cmp_words = words[1:] + ['']
        res = ''
        cnt = 1
        for i in range(len(words)):
            if words[i] == cmp_words[i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += words[i]
                else:
                    res += str(cnt) + words[i]
                    cnt = 1
        ans = min(ans, len(res))
    return ans

print(solution("ababcdcdababcdcd"))
