sample_dict = {
    "name": "Kelly",
    "surname": "Jones",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# for key in sample_dict:
#     print(f"{key:<10} = {sample_dict[key]:>10}")

# for key, value in sample_dict.items():
#     print(f"{key:<10} = {value:>10}")

list = ['age', 'name', 'city']
for key in list:
    sample_dict.pop(key)
print(sample_dict)
