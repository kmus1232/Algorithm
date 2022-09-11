def solution(record):
    preprocess = []
    id_to_name = dict()
    for data in record:
        data_process(data, id_to_name, preprocess)

    result = make_result(preprocess[:], id_to_name)
    return result


def data_process(data, id_to_name, res):
    if data.startswith("Enter"):
        id, name = data.split()[1:]
        id_to_name[id] = name
        res.append([id, "님이 들어왔습니다."])
    elif data.startswith("Leave"):
        id = data.split()[1]
        res.append([id, "님이 나갔습니다."])
    elif data.startswith("Change"):
        id, new_name = data.split()[1:]
        id_to_name[id] = new_name


def make_result(preprocess, id_to_name):
    for i in range(len(preprocess)):
        user_id, message = preprocess[i]
        preprocess[i] = id_to_name[user_id] + message

    return preprocess
