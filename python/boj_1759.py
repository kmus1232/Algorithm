def combination(input_arr, n):
    rst = []

    def dfs(cnt, start, tmp):
        if cnt == n:
            rst.append(tmp)
            return

        for i in range(start, len(input_arr)):
            dfs(cnt + 1, i + 1, tmp + [input_arr[i]])

    dfs(0, 0, [])
    return rst


l, _ = map(int, input().split())
arr = input().split()
consonant = [c for c in arr if c not in "aeiou"]
vowel = [c for c in arr if c in "aeiou"]
result = []

for i in range(2, l):
    j = l - i

    if len(consonant) >= i and len(vowel) >= j:
        for comb_consonant in combination(consonant, i):
            for comb_vowel in combination(vowel, j):
                result.append(sorted(comb_consonant + comb_vowel))

for e in sorted(result):
    print(''.join(e))
