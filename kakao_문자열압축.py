def solution(s):
    ans = len(s)
    for l in range(1, len(s) // 2 + 1):
        compress_result = compress(s, l)
        ans = min(ans, compress_result)
    return ans


def compress(s: str, l: int) -> str:
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
    return res
