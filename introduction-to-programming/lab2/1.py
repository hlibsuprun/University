age = int(input('Wprowadź wiek klienta:'))

if age < 4:
    price = 0
elif 4 <= age <= 18:
    price = 10
else:
    price = 20

print(f'Cena biletu: {price}pł')
