values = [10, 20, 30]
keys = ['ten', 'twenty', 'thirty']

print(list(zip(keys, values)))

# dict = dict(zip(keys, values))

dict1 = {}
for i in range(len(keys)):
    dict1[keys[i]] = values[i]
print(dict1)

dict2 = dict(thirty=30, fourty=40, fifty=50)
print(dict2)

dict3 = dict1.copy()
dict3.update(dict2)
print(dict3)
