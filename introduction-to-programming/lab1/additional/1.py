# a(x)
def a(x):
    if x > 0:
        return 2 * x
    elif x == 0:
        return 0
    elif x < 0:
        return -3 * x


# b(x)
def b(x):
    if x >= 1:
        return x ** 2
    elif x < 1:
        return x


# c(x)
def c(x):
    if x > 2:
        return 2 + x
    elif x == 2:
        return 8
    elif x < 2:
        return x - 4


# TESTS
# a(x)
print('a(2):', a(2))
print('a(0):', a(0))
print('a(-2):', a(-2))
print()

# b(x)
print('b(3):', b(3))
print('b(0):', b(0))
print()

# c(x)
print('c(3):', c(3))
print('c(2):', c(2))
print('c(1):', c(1))
