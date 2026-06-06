# Lesson Name: Array Problems 3
# Goal: Practice array modifications.
# Program to find the max profit you can get from buying and selling stocks. You are given an array with stocks price for seven days, and you can buy and sell any day. 
 
def calculateProfits(arr,arr_size):
 
    profit = 0
    for i in range(1, arr_size):
 
        # If the current element is greater than last element then we will but the previous day and sell it the current day.
        if arr[i] > arr[i-1]:
 
            # calculate profit
            profit += arr[i] - arr[i-1]
 
    return profit
 
# Prices for 7 days
prices = [635,864,247,325,257,745,245]
 
profit = calculateProfits(prices, len(prices))
print("Max profit : ",profit)


# Program to find the amount of water that we can trap within a given set of bars.
 
def findWater(a, a_size):
 
    # Make array to hold the height of left tallest bar for any ith bar
    leftTallest = [0]*a_size
 
    # Make array to hold the height of the right tallest bar for any ith bar
    rightTallest = [0]*a_size
 
    # Initialize result
    water = 0
 
    # Fill left array
    leftTallest[0] = a[0]
    for i in range( 1, a_size):
        leftTallest[i] = max(leftTallest[i-1], a[i])
 
    # Fill right array
    rightTallest[a_size-1] = a[a_size-1]
    for i in range(a_size-2, -1, -1):
        rightTallest[i] = max(rightTallest[i + 1], a[i])
 
    # Water trapped for any ith bar should be minimun of the left and right highest bar - bar height
    for i in range(0, a_size):
        water += min(leftTallest[i], rightTallest[i]) - a[i]
 
    return water
 
a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
bars = len(a)
print("Water : ", findWater(a, bars))
 



arr = [1, 2, 3, 4]
arr.reverse()
print(arr)

arr = [5, 2, 8, 1]
arr.sort()
print(arr)

arr = [10, 20, 30]
arr.append(40)
print(arr)

# Summary:
# Practiced updating and arranging arrays.
