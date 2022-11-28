age = int(input('Enter the age of the client:'))

if age < 4:
    price = 0
elif 4 <= age <= 18:
    price = 10
else:
    price = 20

print(f'Ticket price: {price}pł')
