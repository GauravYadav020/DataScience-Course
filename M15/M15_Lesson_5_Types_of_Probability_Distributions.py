# M15 Lesson 5 – Types of Probability Distributions
# Short Description: Introduction to common probability distributions like Binomial, Poisson, Normal.

# Activity 1
# Goal: Understand and work with Binomial Distribution.
# Summary: Calculate probabilities for binomial experiments.
print("Activity 1: Binomial Distribution")
import scipy.stats as stats

# calculate the probability
prob = 1 - stats.binom.cdf(6, 10, 0.5)

print("the probability of getting more than 6 heads in 10 coin flips is :", prob)
# Activity 2
# Goal: Explore Poisson Distribution for rare events.
# Summary: Solve problems involving count of events in fixed interval.
print("Activity 2: Poisson Distribution")
import scipy.stats as stats

# expected value = 10, probability of observing 6
prob1 = stats.poisson.pmf(6, 10)
print("probability of raining for exactly 6 days :", prob1)

# expected value = 10, probability of observing 12-14
prob2 = stats.poisson.pmf(12, 10) + stats.poisson.pmf(13, 10) + stats.poisson.pmf(14, 10)
print("probability of raining for 12-14 days :", prob2)
# Activity 3
# Goal: Introduce Normal Distribution and its properties.
# Summary: Work with z-scores and standard normal distribution.
print("Activity 3: Normal Distribution")
import scipy.stats as stats

## Checkpoint 1
# calculate prob_more_than_20
prob1 = 1-stats.poisson.cdf(20, 15)

# print prob_more_than_20
print(prob1)

## Checkpoint 2
# calculate prob_17_to_21
prob2 = stats.poisson.cdf(21, 15) - stats.poisson.cdf(16, 15)

# print prob_17_to_21
print(prob2)