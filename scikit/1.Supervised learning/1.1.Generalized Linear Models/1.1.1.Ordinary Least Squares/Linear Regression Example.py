#coding=utf8
__author__ = 'Frank'
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model

diabetes = datasets.load_diabetes()
diabetes_X = diabetes.data[:,np.newaxis,2]
# Split the data into training/testing sets
diabetes_X_train = diabetes_X[:-20]
diabetes_X_test = diabetes_X[-20:]
# Split the targets into training/testing sets
diabetes_y_train = diabetes.target[:-20]
diabetes_y_test = diabetes.target[-20:]

regr = linear_model.LinearRegression()
regr.fit(diabetes_X_train, diabetes_y_train)
# The coefficients
print("Coefficients: \n", regr.coef_)
#print('Residues: \n', regr.residues_ )
#print('Intercept: \n', regr.intercept_ )
# The mean squared error
print("Mean squared error: %.2f"
      % np.mean((regr.predict(diabetes_X_test) - diabetes_y_test) ** 2))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % regr.score(diabetes_X_test, diabetes_y_test))
#print regr.get_params()
# Plot outputs
plt.scatter(diabetes_X_test, diabetes_y_test,  color='black')
plt.plot(diabetes_X_test, regr.predict(diabetes_X_test), color='blue',
         linewidth=3)
plt.xticks(())
plt.yticks(())
plt.show()