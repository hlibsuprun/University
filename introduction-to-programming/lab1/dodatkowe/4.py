array = [0, 0, 0]
status = False

array[0] = int(input("x: "))
array[1] = int(input("y: "))
array[2] = int(input("z: "))
print(array)

i = 0
while status != True:
    for i in range(0, 2):
        if array[i] < array[i + 1]:
            status = True
            continue
        elif array[i] > array[i + 1]:
            status = False
            array[i], array[i + 1] = array[i + 1], array[i]
            break
        else:
            continue

print(array)
