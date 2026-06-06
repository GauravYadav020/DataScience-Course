# Lesson Name: Recursive Problems 1
# Program to reverse a number using recursion 
 
def reverseNumber(num):
    if(num > 0):
        # if the input number is not 0 then get the last digit and add to the current reversesd number received
        last = num%10
        if(num//10>0):
            current_number = reverseNumber((int)(num // 10))
            return last*pow(10,len(str(current_number))) + current_number
        return num
 
n = int(input("Enter your number : "))
print("Reversed : ",reverseNumber(n))


# Program to reverse a string using Recursion
 
def reverseString(s):
 
    # if only 1 char remains just return it
    if len(s) == 1:
        return s[0]
    
    firstchar = s[0]
    # get the already reversed string and add first char to end
    return reverseString(s[1:]) + firstchar
    
 
s = "Ankit Jadli"
print(reverseString(s))


# Program to send if the number is power of 4 or not
 
# Take input
n = int(input("Enter your number : "))
 
def checkIfPower(n):
    # if n is less than equal to 0 just say no
    if(n<=0):
        return False
    # if we reach lowest power of n just retur true
    if(n==1):
        return True
    if(n%4==0):
        return checkIfPower(n/4)
    return False
 
if(checkIfPower(n)):
    print("Power of 4")
else:
    print("Not power of 4")

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
