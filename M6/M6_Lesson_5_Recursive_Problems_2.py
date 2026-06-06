# Lesson Name: Recursive Problems 2
def ways(stairs):
 
    # Check corner case
    if stairs<0:
        return 0
    # If no stair left, just return one as we reach the top
    if stairs==0:
        return 1
    twoSteps=0
    oneStep=0
 
    # We can jump 2 only 2 or more stairs are left
    if (stairs>=2):
        twoSteps = ways(stairs-2)
    # jump 1 if 1 or more staris remains
    oneStep = ways(stairs-1)
    # return total ways
    return twoSteps+oneStep
 
stairs = int(input("Enter number of steps : "))
 
print("Number to ways to climb : ",ways(stairs))

 
def paren(s,l,r,p,n):
    # if we reach end of list just print it and return
    if(p==2*n):
        for ss in s:
            print(ss,end='')
        print("\n")
        return
    # if left parentheses is greater then we can print right one 
    if(l>r):
        s[p]="}"
        paren(s,l,r+1,p+1,n)
    # Left perentheses should not exceed n 
    if(l<n):
        s[p]="{"
        paren(s,l+1,r,p+1,n)
 
 
n = int(input("Enter number of parenthesis : "))
s = [""]*2*n
print("\n")
paren(s,0,0,0,n)


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
