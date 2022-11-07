import random

# distance = float(input('Enter distance:'))
distance = random.randint(1, 1000)
print(f'Random distance: {distance}')
average_fuel_consumption = float(input('Enter average fuel consumption:'))

estimated_fuel_consumption = distance / average_fuel_consumption
estimated_costs = estimated_fuel_consumption * 6.5

print(f'Estimated fuel consumption: {estimated_fuel_consumption}')
print(f'Estimated costs: {estimated_costs}')
