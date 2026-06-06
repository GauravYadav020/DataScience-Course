# M17 Lesson 2 – The Line makes a difference (Logistic Regression)
# Short Description: Understanding Logistic Regression for binary classification and the concept of decision boundary.

# Activity 1
# Goal: Implement Logistic Regression using scikit-learn.
# Summary: Train a simple logistic regression model on a sample dataset.
# Step 1: Import packages, functions, and classes
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix

# Step 2: Get data
x = np.arange(10).reshape(-1, 1)
y = np.array([0, 1, 0, 0, 1, 1, 1, 1, 1, 1])

# Step 3: Create a model and train it
model = LogisticRegression(solver='liblinear', C=10.0, random_state=0)
model.fit(x, y)

# Step 4: Evaluate the model
p_pred = model.predict_proba(x)
y_pred = model.predict(x)
score_ = model.score(x, y)
conf_m = confusion_matrix(y, y_pred)
report = classification_report(y, y_pred)

print('x:', x, sep='\n')

print('y:', y, sep='\n', end='\n\n')

print('intercept:', model.intercept_)

print('coef:', model.coef_, end='\n\n')

print('p_pred:', p_pred, sep='\n', end='\n\n')

print('y_pred:', y_pred, end='\n\n')








# Activity 2
# Goal: Visualize the decision boundary created by Logistic Regression.
# Summary: Plot the line that separates the classes.
from sklearn.datasets import make_classification
from matplotlib import pyplot as plt
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
import pandas as pd

# Generate and dataset for Logistic Regression
x, y = make_classification(
    n_samples=100,
    n_features=1,
    n_classes=2,
    n_clusters_per_class=1,
    flip_y=0.03,
    n_informative=1,
    n_redundant=0,
    n_repeated=0
)

# Create a scatter plot
plt.scatter(x, y, c=y, cmap='rainbow')
plt.title('Scatter Plot of Logistic Regression')
plt.show()

# Split the dataset into training and test dataset
x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=1)

# Create a Logistic Regression Object, perform Logistic Regression
log_reg = LogisticRegression()
log_reg.fit(x_train, y_train)

# Show to Coeficient and Intercept
print(log_reg.coef_)
print(log_reg.intercept_)

# Perform prediction using the test dataset
y_pred = log_reg.predict(x_test)

print(y_pred)