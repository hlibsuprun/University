numbers = map(lambda num: num.strip(), input('Enter 5 numbers separated comma: ').split(','))

for number in numbers:
    if int(number) % 2 == 0 or int(number) % 3 == 0:
        print(number, end=" ")
