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


def tailrec(n, num):
    # Base case: if n exceeds num, terminate the recursion
    if n > num:
        return
    # Print the current value of n
    print(n)
    # Recursive call with the next value (tail recursion)
    tailrec(n + 1, num)

# Prompt the user to enter the value of n
n = int(input("Enter n to print 1 to n: "))

# Initial call to the tailrec function starting from 1
tailrec(1, n)



# Program to print number decreasing then increasing order
 
def incdec(n,num):
    # Base case to return value when we reach our limit
    if(n<1 or n>num):
        return
    # Print decreasing first
    print(n)
    incdec(n-1,num)
    # Print increasing order 
    print(n)
 
n = int(input("Enter any number n : "))
incdec(n,n)
