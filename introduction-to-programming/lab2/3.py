operation_number = int(input('Enter the operation number:'))

if operation_number > 5:
    print('Invalid operation number')
    exit()

first_argument = int(input('Enter the first argument:'))
second_argument = int(input('Enter the second argument:'))

if operation_number == 4 and second_argument == 0:
    print("We can't divide by zero")
    exit()

if operation_number == 1:
    result = first_argument + second_argument
elif operation_number == 2:
    result = first_argument - second_argument
elif operation_number == 3:
    result = first_argument * second_argument
elif operation_number == 4:
    result = first_argument / second_argument
elif operation_number == 5:
    result = first_argument ** second_argument

print(f'Result: {result}')
