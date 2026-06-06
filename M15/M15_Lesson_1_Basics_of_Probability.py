# M15 Lesson 1 – Basics of Probability
# Short Description: Introduction to fundamental concepts of probability, including experiments, events, and basic calculations.

# Activity 1
# Goal: Understand the basic definition of probability and calculate simple probabilities.
# Summary: Students will define probability and compute it for coin toss and dice roll examples.
print("Activity 1: Basic Probability Calculation")
# Write code here for coin toss probability

# Activity 2
# Goal: Differentiate between theoretical and experimental probability.
# Summary: Perform experiments to compare theoretical probability with experimental results.
print("Activity 2: Theoretical vs Experimental Probability")
# Simulate dice rolls

# Activity 3
# Goal: Identify sample spaces and events in probability problems.
# Summary: List sample spaces for given scenarios and identify favorable outcomes.
print("Activity 3: Sample Space and Events")
import random

def pick_ball_experiment():
	# defining our balls as lists
	balls = ['Blue', 'Red', 'Green']

	# "flipping" coins randomly
	result = random.choice(balls)

	#Finding the probability 
	pro = balls.count('Red')/len(balls)
	print("Probability of Picking Red Ball is:", pro)

	# checking if red ball was picked
	if result == 'Red':
		return 'Red Ball was Picked'
	else:
		return 'Better Luck Next Time'
		
res = pick_ball_experiment()
print(res)	
# Example: Rolling two dice