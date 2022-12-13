# def z3(*args):
#     for arg in args:
#         print(arg, end=' ')
#     print()
#
#
# z3(1, 2, 5, 3)

def z3(*args):
    max_num = args[0]
    for arg in args[1:]:
        if arg > max_num:
            max_num = arg
    return max_num


print(z3(1, 2, 5, 10, 3))
