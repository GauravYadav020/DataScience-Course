# Lesson Name: Recursion on List
# Program to recursively check if a given array is sorted or not
 
 
def checkSorted(a):
 
    # Calculating length of array
    length = len(a)
 
    # If array length is 0,1 means we need not to check further
    if length == 1 or length == 0:
        return True
 
    # return true if both below conditions are true
    return a[0] <= a[1] and checkSorted(a[1:])
 
 
a = [1,2,3,5,6,8,2]
 
# Displaying result
if checkSorted(a):
    print("\nYes given array is sorted")
else:
    print("\nNo given array is not sorted")


# Recursively calculate the sum of all elements of the given list
 
def arrayTotalSum(a):
 
    # Calculating length of array
    length = len(a)
 
    # If array length is 1 just return the element
    if length == 1:
        return a[0]
 
    # return current element and received sum 
    return a[0] + arrayTotalSum(a[1:])
 
a = [1,2,3,6]
 
# Displaying result
print("Array total sum: ",arrayTotalSum(a))


# Recursively find the largest number in the array
 
def MaxElementArray(a):
 
    # Calculating length of array
    length = len(a)
 
    # If array length is 1 just return the element
    if length == 1:
        return a[0]
 
    # Return the largest number among current largest and current element
    return max(a[0],MaxElementArray(a[1:]))
 
a = [1,2,234,234,745,3,6,653]
 
# Displaying result
print("Largest element of array: ",MaxElementArray(a))

# Goal:
# Apply recursion on list data structures.

def list_sum(lst):
    if len(lst) == 1:
        return lst[0]
    return lst[0] + list_sum(lst[1:])

print(list_sum([1,2,3,4]))

def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    m = find_max(lst[1:])
    return lst[0] if lst[0] > m else m

print(find_max([4,9,2,7]))

def count_items(lst):
    if lst == []:
        return 0
    return 1 + count_items(lst[1:])

print(count_items([10,20,30,40]))

# Summary:
# Used recursion to process list elements one by one.
