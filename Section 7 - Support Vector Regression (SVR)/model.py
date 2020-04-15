# -*- coding: utf-8 -*-
"""
Created on Thu Jun 20 20:22:40 2019

@author: n_kon
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the Dataset
dataset = pd.read_csv('Position_Salaries.csv')
X = dataset.iloc[:, 1:2].values
y = dataset.iloc[:, 2:3].values

# Splitting the dataset into the Training and Test set
"""From sklearn.cros_validation import traint_test_split
X_train, X_test, y_train, y_,test = train_test_split(X, y, test_size = 0.2, random_state = 0)"""

#Feature Scaling
# Here we still neeed to have the scaling because SVR does not have that 
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
sc_y = StandardScaler()
X = sc_X.fit_transform(X)
y = sc_y.fit_transform(y)

# Fitting the Regression Model to the dataset
# Create your Regression model
from sklearn.svm import SVR
regressor = SVR(kernel = 'rbf')
regressor.fit(X,y)


# Predicting a new result
y_pred = sc_y.inverse_transform(regressor.predict(sc_X.transform([[6.5]])))
y_pred_2 = regressor.predict([[6.5]])


# Visualizing the Resgression results
plt.scatter(X, y, color = 'red')
plt.plot(X, regressor.predict(X), color = 'blue')
plt.title('Truth or Bluff (Regression Model)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()

#Visualizing the SVR  at Higher resolution
X_grid = np.arange(min(X), max(X), 0.01)
X_grid = X_grid.reshape((len(X_grid), 1))
plt.scatter(X, y, color = 'red')
plt.plot(X_grid, regressor.predict(X_grid), color = 'blue')
plt.title('Truth or BLuff (SVRModel)')
plt.xlabel('Position Level')
plt.ylabel('Salary')
plt.show()