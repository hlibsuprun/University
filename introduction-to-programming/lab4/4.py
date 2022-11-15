import random

marks = []

# for i in range(15):
#     marks.append(round(random.uniform(0, 50), 2))

marks = [round(random.uniform(0, 50), 2) for i in range(15)]

print(marks)
