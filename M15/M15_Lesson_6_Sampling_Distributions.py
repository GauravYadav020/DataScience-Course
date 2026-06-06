# M15 Lesson 6 – Sampling Distributions
# Short Description: Understand sampling distributions and Central Limit Theorem.

# Activity 1
# Goal: Generate sampling distribution of sample mean.
# Summary: Simulate repeated sampling to observe distribution shape.
print("Activity 1: Sampling Distribution of Mean")
import numpy as np

#Below is an array that represents the puppies we have in our sample, where 1 
#represents the puppies with blue eyes, and 0 represents the puppies with hazel eyes.

np.random.seed(42)

puppies = np.array([1,0,1,1,1,1,0,0,0,0,1,1,1,1,1,1,1,1,1,1])

#Finding the proportion of puppies with blue eyes in the above array. 
#Storing this value in a variable p

p=puppies.mean()
print("Mean", p)
print("Standard Deviation", puppies.std())
print("Variance", puppies.var())

#Using numpy's random.choice to simulate 5 draws from the puppies array.
np.random.choice(puppies, size=(1,5), replace=True)
np.random.choice(puppies, size=(1,5), replace=True).mean()

#Proportion of sample with blue eyes in 0.8

#Repeating the above to obtain 10,000 additional proportions, where 
#each sample was of size 5. Storing these in a variable called sample_props
print("\nSampling Distribution with size 5 \n")
sample_props= []
for i in range(10000):
    sample = np.random.choice(puppies, 5, replace=True)
    sample_props.append(sample.mean())
sample_props = np.array(sample_props)

#The mean of the sampling distribution
sm = sample_props.mean()
print("Mean", sample_props.mean())
print("Standard Deviation", sample_props.std())
print("Variance", sample_props.var())

print("\nSampling Distribution with size 20 \n")

#Let's repeat all these steps with a new sample, this time size 20.
twenty_sample_props= []
for i in range(10000):
    sample = np.random.choice(puppies, 20, replace=True)
    twenty_sample_props.append(sample.mean())
twenty_sample_props = np.array(twenty_sample_props)

print("New Mean", twenty_sample_props.mean())
print("New Standard Deviation", twenty_sample_props.std())
print("New Variance", twenty_sample_props.var())

# Activity 2
# Goal: Apply Central Limit Theorem in practice.
# Summary: Demonstrate how sample means approach normal distribution.
print("Activity 2: Central Limit Theorem")
import numpy
import matplotlib.pyplot as plt

# number of sample
num = [1, 10, 50, 100]
# list of sample means
means = []

# Generating 1, 10, 30, 100 random numbers from -40 to 40
# taking their mean and appending it to list means.
for j in num:
	# Generating seed so that we can get same result
	# every time the loop is run...
	numpy.random.seed(1)
	x = [numpy.mean(
		numpy.random.randint(
			-40, 40, j)) for _i in range(1000)]
	means.append(x)
k = 0

# plotting all the means in one figure
fig, ax = plt.subplots(2, 2, figsize =(6,6))
for i in range(0, 2):
	for j in range(0, 2):
		# Histogram for each x stored in means
		ax[i, j].hist(means[k], 10, density = True)
		ax[i, j].set_title(label = num[k])
		k = k + 1
plt.show()

# ACP 3
# Goal: Calculate standard error and confidence intervals basics.
# Summary: Understand variability in sampling distributions.
