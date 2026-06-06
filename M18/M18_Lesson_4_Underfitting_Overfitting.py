# M18 Lesson 4 – Underfitting & Overfitting
# Short Description: Concepts of bias-variance tradeoff, underfitting and overfitting.

# Activity 1
# Goal: Demonstrate underfitting with a simple linear model on non-linear data.
# Summary: Observe high bias situation.
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split

np.random.seed(0)
X = 2 - 3 * np.random.normal(0, 1, 20)
y = X**3 + np.random.normal(0, 3, 20)

X = X[:, np.newaxis]
y = y[:, np.newaxis]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=0
)

def plot_model(degree):
    poly = PolynomialFeatures(degree=degree)

    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    model = LinearRegression()
    model.fit(X_train_poly, y_train)

    y_train_pred = model.predict(X_train_poly)
    y_test_pred = model.predict(X_test_poly)

    plt.figure(figsize=(6, 4))
    plt.scatter(X, y, color='blue', label='Data Points')

    X_curve = np.linspace(min(X), max(X), 100)
    X_curve_poly = poly.transform(X_curve.reshape(-1, 1))
    y_curve = model.predict(X_curve_poly)

    plt.plot(X_curve, y_curve, color='red', label=f'Degree: {degree}')

    plt.title(f'Polynomial Regression (Degree: {degree})')
    plt.xlabel('X')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

    print(
        f"Degree {degree} - Train Error: "
        f"{mean_squared_error(y_train, y_train_pred):.2f}, "
        f"Test Error: {mean_squared_error(y_test, y_test_pred):.2f}"
    )

plot_model(1)
plot_model(3)
plot_model(10)
