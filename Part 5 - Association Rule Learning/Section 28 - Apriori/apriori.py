# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Data Preprocessing
dataset = pd.read_csv('Market_Basket_OptimisationPy.csv', header = None)


transactions = []
transactions2 = []


for i in range(0,7501):
    shop_list=[]
    for j in range(0,20):
        shop_list.append(str(dataset.values[i,j]))
    transactions2.append(shop_list)
    

for i in range(0, 10):
   [print(i,j) for j in range(0, 5)]


for i in range(0, 7501):
    transactions.append([dataset.values[i,j] for j in range(0, 20)])

for i in range(0, 7501):
   transactions.append([str(dataset.values[i,j]) for j in range(0, 20)])

    
    
# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)