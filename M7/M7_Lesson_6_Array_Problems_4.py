# Lesson Name: Array Problems 4
# Goal: Solve mixed array challenges.

import numpy as np
data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]
# create a structured array
students = np.array(students_details, dtype=data_type)   
print("Original array:")
print(students)
print("Sort by height")
print(np.sort(students, order='height'))



arr = [1, 2, 3, 4, 5]
print(arr[:3])

arr = [10, 20, 30, 40]
print(arr[-1])

arr = [4, 8, 12, 16]
average = sum(arr) / len(arr)
print(average)

# Summary:
# Solved different array-based practice problems.
