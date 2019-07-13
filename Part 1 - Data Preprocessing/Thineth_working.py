# -*- coding: utf-8 -*-
"""
Created on Sun Nov 25 21:27:23 2018

@author: Thineth
"""

# This is a working area 

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

dataset = pd.read_csv('Data.csv')
print (dataset)

X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,3].values

from sklearn.preprocessing import Imputer

imputer=Imputer(axis=0)

imputer.fit(X[:,1:3])
X[:,1:3]=imputer.transform(X[:,1:3])

print (X)


from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()

X[:,0]=labelencoder_X.fit_transform(X[:,0])

print(X)


onehotencoder=OneHotEncoder(categorical_features = [0], sparse=False)

X=onehotencoder.fit_transform(X)

print(X)

# split data into Train and Test
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)



from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)

sc_y = StandardScaler()
y_train = sc_y.fit_transform(y_train)





