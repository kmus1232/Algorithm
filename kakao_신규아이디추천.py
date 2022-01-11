def solution(new_id: str)->str:
    one = new_id.lower()

    two = ""
    for c in one:
        if 'a' <= c <= 'z' or '0' <= c <= '9' \
                or c == '.' or c == '-' or c == '_':
            two += c

    three = ""
    three += two[0]
    prev = two[0]
    for curr in two[1:]:
        if curr == '.' and prev == curr:
            continue
        three += curr
        prev = curr

    four = three.strip('.')

    five = 'a' if len(four) == 0 else four

    six = five[:15].rstrip('.') if len(five) >= 16 else five

    seven = six + (3 - len(six)) * six[-1] if len(six) < 3 else six

    return seven


