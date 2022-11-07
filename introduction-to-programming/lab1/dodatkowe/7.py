array = list("qwertyuiopasdfghjklzxcvbnm")
array_2 = list("QWERTYUIOPASDFGHJKLZXCVBNM")
letter = input("Letter: ")

cycle = -1
for i in array:
    cycle = cycle + 1
    if letter == i:
        print(array_2[cycle])
        break
    elif letter != i:
        continue

cycle = -1
for i in array_2:
    cycle = cycle + 1
    if letter == i:
        print(array[cycle])
        break
    elif letter != i:
        continue
