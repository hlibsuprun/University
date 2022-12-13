def znaki(string):
    string = string.replace(' ', '')
    dict = {}
    for item in string:
        if item in dict:
            dict[item] = dict[item] + 1
        else:
            dict[item] = 1
    return dict

print(znaki('znaki napisu'))
