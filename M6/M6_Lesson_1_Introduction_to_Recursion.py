# Lesson Name: Introduction to Recursion

# Goal:
# Understand what recursion is and how a function can call itself.

def countdown(n):
    if n == 0:
        print("Done!")
        return
    print(n)
    countdown(n - 1)

countdown(5)

def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)

def sum_n(n):
    if n == 1:
        return 1
    return n + sum_n(n - 1)

print(sum_n(5))

# Summary:
# Practiced basic recursive functions and understood base case.
