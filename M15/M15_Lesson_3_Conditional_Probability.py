# M15 Lesson 3 – Conditional Probability
# Short Description: Understanding conditional probability and its real-world applications.

# Activity 1
# Goal: Calculate conditional probability using formula P(A|B).
# Summary: Solve problems like drawing cards without replacement.
print("Activity 1: Calculating Conditional Probability")
def a_and_b(a, b):

	if a==1:
		prob_student = 0.3
		if b ==1:
			prob_dining = 0.75
		else:
			prob_dining = 0.25
		print("Probability of a given b:", prob_dining)

	if a==2:
		prob_student=0.7
		if b==1:
			prob_dining = 0.6
		else:
			prob_dining = 0.4
		print("Probability of a given b:", prob_dining)
	
	prob_a_and_b = prob_student*prob_dining
	return round(prob_a_and_b, 3)

print("Check the probability of any event occuring. First enter your choices.")

print("Is the student a Freshman? \n 1. Yes \n 2. No")
a = int(input("Enter your choice (1/2): "))

print("Is student eating in dining hall? \n 1. Yes \n 2. No")
b = int(input("Enter your choice (1/2): "))

print("Here is the probability of both the events occuring :", a_and_b(a, b))

# Activity 2
# Goal: Interpret conditional probability in contingency tables.
# Summary: Analyze given tables to find conditional probabilities.
print("Activity 2: Contingency Table Analysis")
def prob_a_and_b(a, b, total):
	# probability of event a
	prob_a = orange/total

	# probability of event b
	prob_bga = blue/(total-1)

	# probability of intersection of events a and b
	prob_AandB = prob_a * prob_bga

	# add return statement here
	return round(prob_AandB,3)
  

# taking input for total number of orange and blue balls
orange = int(input("Enter number of orange balls "))
blue = int(input("Enter number of blue balls "))
total = orange+blue


# call function for final result
print('Probability of Getting 1st orange and 2nd blue ball: ')
print(prob_a_and_b(orange, blue, total))
# Activity 3
# Goal: Apply Bayes' theorem basics through conditional probability.
# Summary: Understand dependence between events using conditional probability.
print("Activity 3: Dependence and Conditional Probability")
RS = int(input("Enter number of red shirts: "))
BS = int(input("Enter number of blue shirts: "))
WS = int(input("Enter number of white shirts: "))

total = RS+BS+WS

prob_a = BS/total
prob_b = RS/total

prob_bga = prob_b
prob_a_and_b = prob_a*prob_b

print("Probability that the second shirt is red given that the first shirt is blue: ")
print(round((prob_bga),3))

print("Probability that the second shirt is red and the first shirt is blue: ")
print(round((prob_a_and_b),3))
