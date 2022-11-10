number_students = int(input("Wprowadź liczbę studentów:"))

current_student = 1
sum = 0

while True:
    mark = int(input(f"Wpisz ocenę studenta #{current_student}:"))

    if 0 <= mark <= 100:
        sum += mark
        current_student += 1
    if current_student > number_students:
        break

print(sum / number_students)
