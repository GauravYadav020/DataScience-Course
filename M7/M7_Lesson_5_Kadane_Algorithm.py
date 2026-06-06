# Lesson Name: Kadane Algorithm
# Goal: Find the maximum sum subarray.

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current_sum = arr[0]
max_sum = arr[0]

for num in arr[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)

print(max_sum)

# Summary:
# Learned the basic implementation of Kadane's Algorithm.
