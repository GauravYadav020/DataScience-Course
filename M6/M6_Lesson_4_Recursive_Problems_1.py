# Lesson Name: Recursive Problems 1

# Goal:
# Solve common recursive problems.

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print(power(2, 5))

def product_n(n):
    if n == 1:
        return 1
    return n * product_n(n - 1)

print(product_n(4))

# Summary:
# Solved mathematical problems using recursion.
