def find(list, value):
    result = []
    for index in range(len(list)):
        if list[index] == value:
            result.append(index)
    return result


print(find(['John', 'Maks', 'John'], 'John'))
