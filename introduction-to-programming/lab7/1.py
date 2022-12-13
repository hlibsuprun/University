import numpy as np

list = [2 ** i for i in range(7, -1, -1)]

weight = np.array(list)

bin = np.random.randint(low=0, high=2, size=8)
print(bin)

result = weight * bin
print(result.sum())
