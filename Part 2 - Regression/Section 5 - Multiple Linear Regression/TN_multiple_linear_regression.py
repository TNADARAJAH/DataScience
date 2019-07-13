# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 16:07:54 2018

@author: Thineth
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

import os
print (os.getcwd())

dataset = pd.read_csv('50_Startups.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values

from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder = LabelEncoder()
X[:, 3] = labelencoder.fit_transform(X[:, 3])

onehotencoder = OneHotEncoder(categorical_features = [3])
X = onehotencoder.fit_transform(X).toarray()

X = X[:,1:]

from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)

X = np.append(np.ones(shape=(50,1)).astype(int), values = X, axis = 1)

import statsmodels.formula.api as sm

X_opt = X[:, [0, 1, 2, 3, 4, 5]]


"""regressor_OLS = sm.OLS(endog=y, exog = X_opt).fit()

regressor_OLS.summary()
X_opt = X[:, [0, 1, 3, 4, 5]]

regressor_OLS = sm.OLS(endog=y, exog = X_opt).fit()
regressor_OLS.summary()

X_opt = X[:, [0, 3, 4, 5]]
regressor_OLS = sm.OLS(endog=y, exog = X_opt).fit()

regressor_OLS.summary()
X_opt = X[:, [0, 3, 5]]

regressor_OLS = sm.OLS(endog=y, exog = X_opt).fit()
regressor_OLS.summary()"""

def backwardElimination(x, sl):
    numVars = len(x[0])
    for i in range(0, numVars):
        regressor_OLS = sm.OLS(y, x).fit()
        maxVar = max(regressor_OLS.pvalues).astype(float)
        if maxVar > sl:
            for j in range(0, numVars - i):
                if (regressor_OLS.pvalues[j].astype(float) == maxVar):
                    x = np.delete(x, j, 1)
    regressor_OLS.summary()
    return x
 
SL = 0.05

X_Modeled = backwardElimination(X_opt, SL)








