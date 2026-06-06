# M23 Lesson 4 – Lane Line detection
# Short Description: Computer vision technique to detect lane lines for autonomous driving.

# Activity 1
# Goal: Apply Canny edge detection and Hough transform for lane detection.
# Summary: Process road images to identify lane markings.
import pandas as pd
import numpy as np
from sklearn.metrics import r2_score, mean_squared_error
from sklearn.model_selection import KFold

# Read the data and get user inputs
df = pd.read_csv('MARUTI.NS.csv')
user_y = input("What you want to predict?\n1. Open\n2. High\n3. Low\n4. Close\n5. RSI(Buy/Sell)\nInput: ")
user_interval = int(input("Number of interval in which you want data to predict: "))
y = df.loc[user_interval:, user_y]
y.index = np.arange(0, len(y))
x = df.drop(['Date', user_y], axis=1).iloc[:-user_interval, :]

train_accuracy = []
test_accuracy = []
train_rsme = []  # Fixed from train_r_sme to train_rsme
test_rsme = []   # Fixed from test_r_sme to test_rsme
kfolds = []
kfold_accuracy = []

def accuracy_score(y_train, y_pred_train, y_test, y_pred_test):
    print("Accuracy in Training: ", r2_score(y_train, y_pred_train)*100)
    train_accuracy.append(r2_score(y_train, y_pred_train)*100)
    print("Accuracy in Testing: ", r2_score(y_test, y_pred_test)*100)
    test_accuracy.append(r2_score(y_test, y_pred_test)*100)

def rsmse(y_train, y_pred_train, y_test, y_pred_test):
    rsmse_test = mean_squared_error(y_test, y_pred_test, squared=False)
    rsmse_train = mean_squared_error(y_train, y_pred_train, squared=False)
    train_rsme.append(rsmse_train)
    test_rsme.append(rsmse_test)
    print("RSME Train: ", rsmse_train)
    print("RSME Test: ", rsmse_test)

def k_fold(algo, kx, ky, cv):
    kf = KFold(n_splits=cv, random_state=None, shuffle=True)
    kfolds.append(cv)
    scores = []
    model = algo
    for train_index, test_index in kf.split(kx):
        X_train, X_test, Y_train, Y_test = kx.iloc[train_index], kx.iloc[test_index], ky[train_index], ky[test_index]
        model.fit(X_train, np.ravel(Y_train))
        Y_pred_train = model.predict(X_train)
        scores.append(r2_score(Y_train, Y_pred_train))
    print("Accuracy: {}".format(np.mean(scores)*100))
    kfold_accuracy.append(np.mean(scores)*100)