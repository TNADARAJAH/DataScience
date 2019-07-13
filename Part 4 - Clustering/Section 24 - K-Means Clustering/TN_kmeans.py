# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 13:27:23 2018

@author: Thineth
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


dataset = pd.read_csv('Mall_Customers.csv')

X = dataset.iloc[:,[2,3]].values

from sklearn.cluster import KMeans

wcss = []

for i in range(1,11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state = 22)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    print(kmeans.inertia_)

    
plt.plot(range(1,11), wcss)
plt.show()

kmeans = KMeans(n_clusters=4, init='k-means++', random_state = 22)

print(kmeans.cluster_centers_)

y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans==0,0], X[y_kmeans==0,1], s = 100, c = 'red', label = 'cluster1')
plt.scatter(X[y_kmeans==1,0], X[y_kmeans==1,1], s = 100, c = 'blue', label = 'cluster1')
plt.scatter(X[y_kmeans==2,0], X[y_kmeans==2,1], s = 100, c = 'pink', label = 'cluster1')
plt.scatter(X[y_kmeans==3,0], X[y_kmeans==3,1], s = 100, c = 'green', label = 'cluster1')
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1], s = 200, c = 'yellow')


print(y_kmeans==2)
