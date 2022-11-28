from horner import horner
number = int(input('Enter number:'))

poly = [2, 4, 6, 8, 10]
result = horner(poly, 0, len(poly) - 1, number)

print(result)
