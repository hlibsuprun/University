operation = int(input('Wpisz numer operacji:'))

if operation > 5:
    print("Nieprawidłowy numer operacji")
    exit()

first_argument = int(input('Podaj argument 1:'))
second_argument = int(input('Podaj argument 2:'))

if operation == 4 and second_argument == 0:
    print("Nie możemy podzielić przez zero")
    exit()

if operation == 1:
    solution = first_argument + second_argument
elif operation == 2:
    solution = first_argument - second_argument
elif operation == 3:
    solution = first_argument * second_argument
elif operation == 4:
    solution = first_argument / second_argument
elif operation == 5:
    solution = pow(first_argument, second_argument)

print(f"Wynik: {solution}")
