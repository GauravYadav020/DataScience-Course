# ============================================================
# M16 Lesson 1 – Understanding Machine Learning
# ============================================================
# Machine Learning (ML) is a branch of AI where computers learn
# patterns from data without being explicitly programmed.
# Types of ML: Supervised, Unsupervised, and Reinforcement Learning.
# ============================================================

import numpy as np
import matplotlib.pyplot as plt


# ----------------------------
# Activity 1: Types of Machine Learning
# ----------------------------
# Goal: Understand the three types of ML with simple examples.
# Summary: Students will explore Supervised, Unsupervised, and
#          Reinforcement Learning concepts through code demonstrations
#          and printed examples that map to real-world problems.

# Task:
print("=" * 55)
print("       TYPES OF MACHINE LEARNING")
print("=" * 55)

# Supervised Learning – labeled data (input → known output)
print("\n1. SUPERVISED LEARNING")
print("   Data has labels (correct answers provided).")
print("   Examples:")
supervised_examples = {
    "Email Spam Detection":     "Input: Email text  → Output: Spam / Not Spam",
    "House Price Prediction":   "Input: Size, Location → Output: Price (₹)",
    "Disease Diagnosis":        "Input: Symptoms → Output: Disease Name",
    "Student Pass/Fail":        "Input: Marks → Output: Pass / Fail",
}
for task, mapping in supervised_examples.items():
    print(f"   • {task}: {mapping}")

# Unsupervised Learning – no labels, find hidden patterns
print("\n2. UNSUPERVISED LEARNING")
print("   Data has NO labels. Model finds patterns on its own.")
print("   Examples:")
unsupervised_examples = {
    "Customer Segmentation":  "Group customers by buying behavior",
    "News Article Grouping":  "Cluster similar articles together",
    "Anomaly Detection":      "Find unusual transactions in bank data",
}
for task, desc in unsupervised_examples.items():
    print(f"   • {task}: {desc}")

# Reinforcement Learning – learn from rewards and penalties
print("\n3. REINFORCEMENT LEARNING")
print("   Agent learns by trial-and-error using rewards.")
print("   Examples:")
rl_examples = {
    "Game Playing (Chess/Go)": "Win = +reward, Lose = -reward",
    "Self-Driving Cars":       "Safe drive = +reward, Crash = -reward",
    "Robot Navigation":        "Reach goal = +reward, Obstacle = -reward",
}
for task, reward in rl_examples.items():
    print(f"   • {task}: {reward}")


# ----------------------------
# Activity 2: The ML Workflow
# ----------------------------
# Goal: Understand the step-by-step process of building an ML model.
# Summary: Students will walk through all stages of the ML pipeline —
#          from collecting data to evaluating the trained model.

# Task:
print("\n" + "=" * 55)
print("       THE MACHINE LEARNING WORKFLOW")
print("=" * 55)

ml_steps = [
    ("Step 1", "Collect Data",        "Gather raw data from surveys, sensors, databases"),
    ("Step 2", "Prepare Data",        "Clean, handle missing values, encode categories"),
    ("Step 3", "Explore Data (EDA)",  "Visualize patterns, correlations, distributions"),
    ("Step 4", "Choose a Model",      "Pick algorithm: Linear Regression, Decision Tree…"),
    ("Step 5", "Train the Model",     "Feed training data so the model learns patterns"),
    ("Step 6", "Evaluate the Model",  "Test on unseen data, measure accuracy/error"),
    ("Step 7", "Improve the Model",   "Tune parameters, add features, try other models"),
    ("Step 8", "Deploy the Model",    "Integrate into an app or API for real-world use"),
]

for step, title, description in ml_steps:
    print(f"\n  {step}: {title}")
    print(f"          → {description}")


# ----------------------------
# Activity 3: Visualize the Concept of Learning from Data
# ----------------------------
# Goal: Simulate how ML "learns" a pattern from data points visually.
# Summary: Students will generate noisy data with a known pattern,
#          plot it, and see how a model (best-fit line) captures the trend.

# Task:
np.random.seed(42)
X = np.linspace(1, 10, 30)
y = 3 * X + 5 + np.random.randn(30) * 4     # True pattern: y = 3x + 5 + noise

# Fit a line (simulate "learning")
coeffs = np.polyfit(X, y, 1)
y_pred = np.polyval(coeffs, X)

plt.figure(figsize=(8, 5))
plt.scatter(X, y, color="steelblue", s=60, label="Observed Data (with noise)", zorder=3)
plt.plot(X, y_pred, color="red", linewidth=2.5, label=f"Learned Line: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
plt.plot(X, 3 * X + 5, color="green", linestyle="--", linewidth=1.5, label="True Pattern: y = 3x + 5")
plt.title("ML Concept: Learning a Pattern from Noisy Data")
plt.xlabel("Input (X)")
plt.ylabel("Output (y)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

print(f"\nLearned equation: y = {coeffs[0]:.2f}x + {coeffs[1]:.2f}")
print(f"True equation:    y = 3.00x + 5.00")
print("→ The model came very close to the true pattern just from data!")
