def horner(L, left, right, x):
    i = right
    result = L[i]
    while i > left:
        i = i - 1
        result = result * x + L[i]
    return result
