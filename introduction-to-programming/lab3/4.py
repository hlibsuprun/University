first_number = int(input("Wprowadź pierwszą liczbę:"))
second_number = int(input("Wpisz drugą liczbę:"))

numbers_string = ""
current_number = min(first_number, second_number)

while current_number <= max(first_number, second_number):
    if current_number % 2 == 0:
        numbers_string += f" {current_number}"
    current_number += 1

print(numbers_string)
