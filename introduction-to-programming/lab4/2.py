import random

list = []
amount = int(input("Enter amount:"))

for number in range(amount):
    list.append(random.randint(1, 10))

print(list)

amount2 = int(input("Enter amount:"))
list2 = [random.randint(5, 15) for num in range(amount2)]
print(amount2)

number = int(input("Enter number:"))
if number in list:
    print("The number is in the first list")
elif number in list2:
    print("The number is in the second list")
else:
    print("No number in both lists")

combined_lists = list + list2
print(combined_lists)
