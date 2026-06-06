# Mean of an array = sum of elements / number of elements
def arrayMean(arr, arr_size):
 
    total_sum = 0
    for i in range(0, arr_size):
        total_sum += arr[i]
 
    return float(total_sum/arr_size)
 
# Median for a sorted array depends if size is even or odd
def arrayMedian(arr, arr_size):
 
    # Sort array 
    sorted(arr)
 
    # Return element for even and odd sized array
    if arr_size % 2 != 0:
        return float(arr[int(arr_size/2)])
 
    return float((arr[int((arr_size-1)/2)] +
                arr[int(arr_size/2)])/2.0)
 
 
arr = [1,4,5,2,5,8,5,2,6,8]
arr_size = len(arr)
 
print("Mean =", arrayMean(arr, arr_size))
print("Median =", arrayMedian(arr, arr_size))


# Minimum Function
def minElement(a, size):
    temp = a[0]
    for i in range(1,size):
        temp = min(temp, a[i])
    return temp
 
# Maximum Function
def maxElement(a, size):
    temp = a[0]
    for i in range(1,size):
        temp = max(temp, a[i])
    return temp
 
 
a = [12, 1234, 45, 67, 1]
size = len(a)
print ("Minimum element of array:", minElement(a, size))
print ("Maximum element of array:", maxElement(a, size))
 
# Function to find the number and print it.
def print2largest(a, a_size):
 
    largest = secondLargest = -2147483648
    for i in range(a_size):
     
        # If the current element of the array is greater than our current largest number, then replace
        if (a[i] > largest):
            
            secondLargest = largest
            largest = a[i]
            
 
        # If current element is less than current largest but greater than second largest then replace the number
        elif (a[i] > secondLargest and a[i] != largest):
            secondLargest = a[i]
        
 
    print(secondLargest)
 
 
a = [1,2,3,4,5,6,7,8,9]
a_size = len(a)
print2largest(a, a_size)
