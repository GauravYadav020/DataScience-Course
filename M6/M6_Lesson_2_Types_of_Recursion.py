# Lesson Name: Types of Recursion

# Goal:
# Explore direct and indirect recursion.

def direct(n):
    if n == 0:
        return
    print(n)
    direct(n - 1)

direct(5)

def even(n):
    if n == 0:
        print("Even")
        return
    odd(n - 1)

def odd(n):
    if n == 0:
        print("Odd")
        return
    even(n - 1)

even(4)

def multiply(a, b):
    if b == 0:
        return 0
    return a + multiply(a, b - 1)

print(multiply(4, 3))

# Summary:
# Learned different ways recursive functions can interact.
