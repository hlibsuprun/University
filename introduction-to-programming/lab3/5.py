number_students = int(input('Enter the number of students:'))

current_student = 1
sum = 0

while current_student <= number_students:
    mark = int(input(f"Enter the student's grade #{current_student}:"))
    sum += mark
    current_student += 1

print(sum / number_students)
