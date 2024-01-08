def sorting(list, method):
    for i in range(len(list) - 1):
        for j in range(0, len(list) - i - 1):
            if method(list[j]) > method(list[j+1]):
                list[j], list[j+1] = list[j+1], list[j]
    return list

def searching(list, method):
    result = []
    for elem in list:
        if method(elem):
            result.append(elem)
    if result == []:
        raise ValueError("no elements found.")
    return result
