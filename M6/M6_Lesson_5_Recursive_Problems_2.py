# Lesson Name: Recursive Problems 2

# Goal:
# Practice recursion with pattern-based problems.

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i))

def reverse_string(text):
    if len(text) == 0:
        return ""
    return reverse_string(text[1:]) + text[0]

print(reverse_string("coding"))

def count_char(text):
    if text == "":
        return 0
    return 1 + count_char(text[1:])

print(count_char("python"))

# Summary:
# Practiced recursion with strings and sequences.
