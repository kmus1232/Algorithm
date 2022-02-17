from copy import deepcopy

def match(bid, uid):
    if len(uid) != len(bid):
        return False
    for i in range(len(uid)):
        if bid[i] == '*' or bid[i] == uid[i]:
            continue
        else:
            return False
    return True


def find_possible_cases(match_list_arr):
    if not match_list_arr:
        return [[]]

    result = []
    for case in match_list_arr[0]:
        copy_arr = deepcopy(match_list_arr[1:])
        for match_list in copy_arr:
            if case in match_list:
                match_list.remove(case)
        for possible_case in find_possible_cases(copy_arr):
            result.append([case] + possible_case)
    return result


def solution(user_id, banned_id):
    match_list_arr = []
    for bid in banned_id:
        match_list = []
        for uid in user_id:
            if match(bid, uid):
                match_list.append(uid)
        match_list_arr.append(match_list)

    possible_cases = find_possible_cases(match_list_arr)
    result = set([tuple(sorted(case)) for case in possible_cases])
    return len(result)


print(solution(
    ["frodo", "fradi", "crodo", "abc123", "frodoc"],
    ["fr*d*", "*rodo", "******", "******"]
))