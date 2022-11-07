operation_number = int(input("Enter operation number:"))
first_number = int(input("Enter first number:"))
second_number = int(input("Enter second number:"))

if operation_number > 5:
    print("Invalid operation number")

if operation_number == 4 and second_number == 0:
    print("Can't divide by zero")
    exit()

if operation_number == 1:
    solution = first_number + second_number
elif operation_number == 2:
    solution = first_number - second_number
elif operation_number == 3:
    solution = first_number * second_number
elif operation_number == 4:
    solution = first_number / second_number
elif operation_number == 5:
    solution = first_number % second_number

print(f"Solution: {solution}")
