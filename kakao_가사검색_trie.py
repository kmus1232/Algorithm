def make_trie(words):
    trie = dict()
    for word in words:
        tmp = trie

        while word:
            if len(word) not in tmp:
                tmp[len(word)] = 1
            else:
                tmp[len(word)] += 1

            if word[0] not in tmp:
                tmp[word[0]] = dict()
            tmp = tmp[word[0]]
            word = word[1:]

    return trie


def find_query(trie, q):
    while q[0] != '?':
        if q[0] not in trie:
            return 0
        trie = trie[q[0]]
        q = q[1:]
    if len(q) not in trie:
        return 0
    return trie[len(q)]


def solution(words, queries):
    trie = make_trie(words)
    reverse_trie = make_trie([w[::-1] for w in words])

    result = []
    for q in queries:
        if q[0] == '?':
            result.append(find_query(reverse_trie, q[::-1]))
        else:
            result.append(find_query(trie, q))
    return result


