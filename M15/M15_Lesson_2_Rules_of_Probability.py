# M15 Lesson 2 – Rules of Probability
# Short Description: Learn addition and multiplication rules of probability along with mutually exclusive and independent events.
# Create the two sets of two guest lists
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find union of two sets
union = set1.intersection(set2)

# Converting set into list 
# to find total guests to be invited in party
total_guests = list(union)

print("Total guests to be invited in party are :", len(total_guests))
print("Guest List :", total_guests)

# Create the two sets of two guest lists
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find union of two sets
union = set1.union(set2)

# Converting set into list 
# to find total guests to be invited in party
total_guests = list(union)

print("Total guests to be invited in party are :", len(total_guests))
print("Guest List :", total_guests)



# Create the two sets of two guest lists
set1 = {'A', 'B', 'C', 'D', 'E'}
set2 = {'B', 'D', 'V', 'X', 'Y', 'Z'}

# Find union of two sets
union = set1.intersection(set2)

# Converting set into list 
# to find total guests to be invited in party
total_guests = list(union)

print("Total guests to be invited in party are :", len(total_guests))
print("Guest List :", total_guests)



# ACP task 1
# Goal: Apply the addition rule for probability of union of events.
# Summary: Calculate probabilities using addition rule for mutually exclusive and non-exclusive events.
print("ACP task 1: Addition Rule of Probability")

# ACP task 2
# Goal: Use multiplication rule for independent and dependent events.
# Summary: Solve problems involving joint probabilities of independent events.
print("ACP task 2: Multiplication Rule")

# ACP task 3
# Goal: Understand complementary events and their probabilities.
# Summary: Calculate probability of complement of an event in real-life scenarios.
print("ACP task 3: Complementary Events")