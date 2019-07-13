# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 13:00:30 2018

@author: Thineth
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dataset=pd.read_csv('Position_salaries.csv')

X=dataset.iloc[:,2:3].values
y=dataset.iloc[:,2].values

from sklearn.preprocessing import StandardScaler as sc

sc_X = sc()
sc_y = sc()

X=sc_X.fit_transform(X)
y=sc_y.fit_transform(y)


from sklearn.svm import SVR



regressor = SVR(kernel='rbf')

regressor.fit(X,y)

y_pred = regressor.predict(sc_X.fit_transform([[6.5]]))
y_pred = sc_y.inverse_transform(y_pred)

plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Position/Salary')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()

X_grid = np.arange(min(X), max(X), 0.1)
X_grid = X_grid.reshape((len(X_grid),1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Position/Salary - HD')
plt.xlabel('Level')
plt.ylabel('Salary')
plt.show()
