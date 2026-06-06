# Lesson Name: Recursion on List

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
