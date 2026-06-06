# Lesson Name: Array Problems 2
# Goal: Work with searching and counting.

arr = [1, 2, 3, 4, 5]
print(3 in arr)

arr = [1, 2, 2, 3, 2]
print(arr.count(2))

arr = [10, 20, 30, 40]
print(arr.index(30))

# Summary:
# Learned searching and counting techniques.


# Program to reverse an array in the group of 'n.'
 
# Accept array, its size and group size
def reverse(a, a_size, n):
    temp = 0
    
    while(temp<a_size):
    
        start = temp
 
        # When a_size/n is not divisible
        end = min(temp + n - 1, a_size - 1)
 
        # Reverse the sub-array [start, right]
        while (start < end):
            
            a[start], a[end] = a[end], a[start]
            start+= 1;
            end-=1
        temp+= n
    
a = [5,23,5,23,1,23,5,136,7,56]
 
n = 2
a_size = len(a)
reverse(a, a_size, n)
 
for i in range(0, a_size):
        print(a[i], end =" ")


# Program to rotate an array 'n' times to the left
 
# Input array, length  and 'n'
def rotations(a, n, a_size):
    for i in range(n):
        rotate(a, a_size)
 
# Rotate array to the left by 1 place
def rotate(a, a_size):
    temp = a[0]
    for i in range(a_size-1):
        a[i] = a[i + 1]
    a[a_size-1] = temp
        
 
def printArray(a, a_size):
    for i in range(a_size):
        print ("% d"% a[i], end =" ")
    print("\n")
 
 
a = [12,12,31,85,2,3,53,56323]
printArray(a,len(a))
rotations(a, 2, len(a))
printArray(a, len(a))


def leaders(a, a_size):
    # Right most is always a leader
    currentmax = a[a_size-1]
    print(currentmax)
    
    # Check from 2nd last element if it is grater than currentmax is yes that number is a leader and our new currentmax too.
    for i in range( a_size-2, -1, -1):  
        if currentmax < a[i]:   
            print(a[i])
            currentmax = a[i]
        
 
a = [16, 17, 4, 3, 5, 245]
leaders(a, len(a))
