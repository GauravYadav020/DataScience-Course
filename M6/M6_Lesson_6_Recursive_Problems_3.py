# Lesson Name: Recursive Problems 3

# Goal:
# Use recursion to solve advanced logical problems.

def palindrome(text):
    if len(text) <= 1:
        return True
    if text[0] != text[-1]:
        return False
    return palindrome(text[1:-1])

print(palindrome("madam"))

def digit_sum(n):
    if n < 10:
        return n
    return n % 10 + digit_sum(n // 10)

print(digit_sum(1234))

def find_min(lst):
    if len(lst) == 1:
        return lst[0]
    m = find_min(lst[1:])
    return lst[0] if lst[0] < m else m

print(find_min([8,3,12,1,9]))

# Summary:
# Applied recursion to solve logical and data-based problems.
