# Lesson Name: Recursive Problems 3
# Program to find all the possible combinations when we press keys in phone keypad
 
 
keypad = ["", "", "abc", "def", "ghi", "jkl",
            "mno", "pqrs", "tuv", "wxyz"]
 
def printCombination(combination, curr, output, n):
    if(curr == n):
        print(*output,sep=",")
        return
    # Print all the possible combination by iterating first 1 to 3 for number an finding that index in keypad.
    for i in range(len(keypad[combination[curr]])):
 
        output.append(keypad[combination[curr]][i])
 
        printCombination(combination, curr + 1, output, n)
        output.pop()
        if(combination[curr] == 0 or combination[curr] == 1):
            return
 
 
 
 
combination = [4, 3, 4]


n = len(combination)
printCombination(combination, 0, [], n)
 
# Program to move n disks in Tower of Hanoi 
 
def Hanoi(n , a, b, c):
    if n == 1:
        print("Move disk 1 from rod",a,"to rod",b)
        return
    # move n-1 disk from a to b
    Hanoi(n-1, a, c, b)
    print("Move disk",n,"from rod",a,"to rod",b)
    Hanoi(n-1, c, b, a)
        
n = 4
Hanoi(n, 'A', 'C', 'B')
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
