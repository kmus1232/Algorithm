from collections import defaultdict

n = int(input())
_ = input()
s = input()

cnt_dict = defaultdict(int)

i = 0
cnt = 0
while i < len(s):
    if s[i] != 'I':
        i += 1
    else:
        while i + 2 < len(s) and (s[i+1] == 'O' and s[i+2] == 'I'):
            i += 2
            cnt += 1
        if cnt > 0:
            cnt_dict[cnt] += 1
            cnt = 0
        i += 1

ans = 0
for cnt, num in cnt_dict.items():
    if cnt >= n:
        ans += (cnt - n + 1) * num
print(ans)

