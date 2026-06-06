# Lesson Name: Kadane Algorithm
# Goal: Find the maximum sum subarray.

# Program to find the maximum consecutive ones in an array of 1's and 0's.
# Program to find max subarray sum
# Standard Kadane's algorithm to find maximum subarray sum
def kadane(a):
    n = len(a)
    max_so_far = 0
    max_ending_here = 0
    for i in range(0, n):
        max_ending_here = max_ending_here + a[i]
        if (max_ending_here < 0):
            max_ending_here = 0
        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
    return max_so_far
 
# The function returns maximum circular contiguous sum in
# a[]
def maxCircularSum(a):
 
    n = len(a)
 
    # apply kadane algo if no circular is needed
    max_kadane = kadane(a)
 
    # Find sum of all element and invert them
    max_wrap = 0
    for i in range(0, n):
        max_wrap += a[i]
        a[i] = -a[i]
 
    # Apply kedance algo to find minimun inverted subarray
    max_wrap = max_wrap + kadane(a)
 
    # The maximum circular sum will be a maximum of two sums
    if max_wrap > max_kadane:
        return max_wrap
    else:
        return max_kadane
 
 
a = [11, 10, -20, 5, -3, -5, 8, -13, 10]
print("Maximum circular sum is", maxCircularSum(a))
 



def maxSubArraySum(a,a_size):
    
    max =  -99999999999
    cmax = 0
    
    # Add current element to current max, check if cmax > max if yes update max, if cmax is less than 0 then reset it to 0
    for i in range(0, a_size):
        cmax = cmax + a[i]
        if (max < cmax):
            max = cmax
 
        if cmax < 0:
            cmax = 0
    return max
 
a = [1,2,3,-4,5,-22,-4,25,2,-9]
print(maxSubArraySum(a,len(a)))

# Returns the result
def getMaxLength(a, a_size):
 
    counter = 0
    maxOnes = 0
 
    for i in range(0, a_size):
    
        # If we find a 0 then reset the counter
        if (a[i] == 0):
            counter = 0
 
        # If we find 1 then increment our counter and update the maxOnes
        else:
            # increase count
            counter += 1
            maxOnes = max(maxOnes, counter)
        
    return maxOnes
 
a = [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
a_size = len(a)
 
print("Max 1's : ",getMaxLength(a, a_size))


# Program to move the 0's to the end
 
def pushZerosToEnd(a, a_size):
 
    # Zero will hold the position where non zero numbers should be
    zero = 0
 
    # Non zero will iterate to find if the current number is zero or non zero
    nonzero = 0
 
    while(nonzero!=a_size):
        if a[nonzero]!=0:
            a[nonzero],a[zero] = a[zero],a[nonzero]
            zero+=1
        nonzero+=1
        
# Driver code
a = [1,0,3,6,0,0,0,2,355,0,72]
a_size = len(a)
print(a)
pushZerosToEnd(a, a_size)
print("Array after pushing all zeros to end of array:")
print(a)



arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

for num in arr[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)

# Summary:
# Learned the basic implementation of Kadane's Algorithm.
