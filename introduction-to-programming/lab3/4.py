first_number = int(input('Enter the first number:'))
second_number = int(input('Enter the second number:'))

numbers_string = ''
current_number = min(first_number, second_number)

while current_number <= max(first_number, second_number):
    if current_number % 2 == 0:
        numbers_string += f' {current_number}'
    current_number += 1

print(numbers_string)
