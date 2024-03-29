# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 19:17:13 2018

@author: Thineth
"""

import numpy as np
import matplotlib.pyplot as ppt
import pandas as pd


dataset = pd.read_csv('Social_Network_Ads.csv')

X = dataset.iloc[:,2:4].values
y = dataset.iloc[:,4].values


from sklearn.cross_validation import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler

sc_X = StandardScaler()

X_train = sc_X.fit_transform(X_train)
X_test = sc_X.fit_transform(X_test)

from sklearn.linear_model import LogisticRegression

classifier=LogisticRegression(random_state=0)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

from sklearn.metrics import confusion_matrix

cm = confusion_matrix(y_test, y_pred)












