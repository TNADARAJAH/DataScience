# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 11:40:28 2018

@author: Thineth
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Position_salaries.csv')

X= dataset.iloc[:,1:2].values
y = dataset.iloc[:,2].values



from sklearn.linear_model import LinearRegression

lin_reg=LinearRegression()
lin_reg.fit(X,y)

from sklearn.preprocessing import PolynomialFeatures

poly_reg = PolynomialFeatures(degree=4)
X_poly=poly_reg.fit_transform(X)
#poly_reg.fit(X_poly,y)

lin_reg2=LinearRegression()
lin_reg2.fit(X_poly,y)

plt.scatter(X,y,color='red')
plt.plot(X,lin_reg.predict(X), color='blue')
plt.xlabel("Level")
plt.ylabel("Salary")
plt.title("Level to salary")
plt.show()

plt.scatter(X,y,color='red')
plt.plot(X, lin_reg2.predict(poly_reg.fit_transform(X)))

plt.show()

X_grid = np.arange(min(X), max(X),0.1)
X_grid2 = X_grid.reshape(len(X_grid), 1)




