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

# Program to print numbers from 1 to 10 using recursion
 
# Recursive function that will accept n till we reach 10 
def print1to10(n):
    # Base case to stop the recursion
    if(n>10):
        return
    print(n)
 
    # Recursive call 1 -> 2 , 2 -> 3, 3 -> 4 and so on
    print1to10(n+1)
 
print1to10(1)


# Program to find factorial of any number using recursion 
def fac(n):
    # When n is 1 or 0, return 1 
    if(n==1 or n==0):
        return 1
    # Factorial of n = n*n-1*n-2...1
    return n*fac(n-1)
n = int(input("Enter your number : "))
print ("Factorial of", n, "is : ",fac(n))
