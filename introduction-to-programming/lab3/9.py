rows = int(input('Enter number: '))

# for row in range(1, rows + 1):
#     for element in range(row):
#         print('*', end='')
#     print()

for row in range(1, rows + 1):
    for space in range(1, rows - row + 1):
        print(' ', end='')
    for element in range(0, row):
        print('*', end=' ')
    print()


