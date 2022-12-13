dict1 = {'data1': 10, 'data2': -4, 'data3': 2}

def sum_of_values(values):
    result = 0
    for value in values.values():
        result += value
    return result


print(sum_of_values(dict1))
