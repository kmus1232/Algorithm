import re

def solution(new_id: str) -> str:
    one = new_id.lower()

    two = re.sub("[^0-9a-z.\-_]", "", one)

    three = re.sub("[.]{2,}", ".", two)

    four = three.strip(".")

    five = "a" if len(four) == 0 else four

    six = five[:15].rstrip(".") if len(five) > 15 else five

    seven = six + (3 - len(six)) * six[-1] if len(six) < 3 else six

    return seven