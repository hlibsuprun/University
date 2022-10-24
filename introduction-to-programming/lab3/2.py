solutions_string = ""
current_number = -4

while current_number < 4:
    solutions_string += f" {2 * current_number ** 2 - 5 * current_number - 8}"
    current_number += 0.5

print(solutions_string)