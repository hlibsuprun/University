import numpy as np

table = np.random.randint(low=0, high=5, size=(5, 5))
print(table)

print(f'max: {table.max()}')
print(f'min: {table.min()}')

print(f'max in rows: {table.max(axis=1)}')
print(f'max in columns: {table.max(axis=0)}')

print(f'sum in rows: {table.sum(axis=1)}')
print(f'sum in columns: {table.sum(axis=0)}')
