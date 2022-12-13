def potęga(list1, list2):
    if len(list1) != len(list2):
        print('Different length of lists')
        exit()

    result = []
    index = 0
    while index < len(list1):
        result.append(list1[index] ** list2[index])
        index += 1
    return result


print(potęga([1, 2, 3], [1, 2, 3]))
