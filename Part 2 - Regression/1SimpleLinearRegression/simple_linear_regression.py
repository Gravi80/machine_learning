# [YearsExperience, Salary]
# Simple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('../dataset/Salary_Data.csv')
features = dataset.iloc[:, :-1].values  # features.shape  = (30, 1) [ Matrix that has 1 column ]
dependent = dataset.iloc[:, 1].values   # dependent.shape = (30,)	[ No columns, i.e its a vector ]


# Splitting the dataset into Training set and Test set
from sklearn.cross_validation import train_test_split
features_train,features_tests,dependent_train,dependent_tests = train_test_split(features,dependent,test_size=(1/3.0), random_state=0)

# No need of Feature Scaling, Python ML library will take care of it


# Fitting Simple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,dependent_train)
# Here the Machine is SimpleLinearRegression model and this model learned on the training set.


# Predicting the test set results
# Will contain predicted salary for all the observations of our test set
dependent_predictions = regressor.predict(features_tests)



# Visualizing Training set results
plt.scatter(features_train,dependent_train,color='red') # plot the real observation points
plt.plot(features_train,regressor.predict(features_train), color='blue') # Regression line, Y is prediction of the features_train
plt.title('Salary vs Experience (Training set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
# Red => Real Value, 
# Blue => Predicted Value


# Visualizing Test set results
plt.scatter(features_tests,dependent_tests,color='red')
plt.plot(features_train,regressor.predict(features_train), color='blue') # Will keep same regression line 
plt.title('Salary vs Experience (Test set)')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.show()
# Red => Value of the test set
# Blue => Original regression line