def dodawanie(f_num, s_num):
    return f_num + s_num


def odejmowanie(f_num, s_num):
    return f_num - s_num


def mnożenie(f_num, s_num):
    return f_num * s_num


def dzielenie(f_num, s_num):
    if s_num != 0:
        return f_num / s_num


first_number = int(input('Enter first number: '))
second_number = int(input('Enter second number: '))
operator = input('Enter operator: ')

dict = {'+': dodawanie, '-': odejmowanie, '*': mnożenie, '/': dzielenie}

print(dict[operator](first_number, second_number))
