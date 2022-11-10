number_students = int(input("Wprowadź liczbę studentów:"))

current_student = 1
sum = 0

while current_student <= number_students:
    mark = int(input(f"Wpisz ocenę studenta #{current_student}:"))
    sum += mark
    current_student += 1

print(sum / number_students)
