# Copy the Regression template from RegressionTemplate.py

# Importing the libraries
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
# np.set_printoptions(threshold=np.nan,formatter={'float': lambda x: "{0:0.0f}".format(x)})

# Importing the dataset
dataset = pd.read_csv('../dataset/Position_Salaries.csv')

# Derive features and dependent variables. Features should always be considered as Matrix
features = dataset.iloc[:, 1:2].values  # features.shape  = (10,1) [ No columns, i.e its a vector ]
dependent = dataset.iloc[:, 2].values   # dependent.shape = (10,)	[ No columns, i.e its a vector ]

# Encoding Categorical data

# Splitting the dataset into Training set and Test set

# Feature Scaling [SVR doesn't apply feature scaling]
# A case of getting all your data on the same scale. 
# The main advantage of scaling is to avoid attributes in greater numeric ranges dominating those in smaller numeric ranges.
from sklearn.preprocessing import StandardScaler
scale_features = StandardScaler()
scale_dependent = StandardScaler()
features = scale_features.fit_transform(features)
dependent = scale_dependent.fit_transform(dependent)

# Fitting SVR model to the dataset
# Create your regressor
from sklearn.svm import SVR
    # kernel => whether you want a Linear/Ploynomial/Gaussian SVR
regressor = SVR(kernel='rbf') # our problem is non-linear
regressor.fit(features,dependent)

# Predicting a new result with SVR model [Around = 160862]
y_pred = regressor.predict(scale_features.fit_transform(np.array([[6.5]]))) # alone [6.5] won't be an array, it will be a vector containing 1 element

    # we need to do Inverse trandform to get the original scale of the salary
y_pred = scale_dependent.inverse_transform(y_pred)

# Visualising SVR model results
plt.scatter(features,dependent,color='red')
plt.plot(features,regressor.predict(features),color='blue')
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
#  SVR model considered CEO as outlier


# Visualising SVR model results (for higher resolution and smoother curve)
features_grid = np.arange(min(features),max(features),0.1) # will contains all the levels from 1 to 10, along with imaginary level 1.1, 1.2 ..... 9.9
features_grid = features_grid.reshape((len(features_grid),1))    # convert feature grid to matrix  reshape(rows,column)
plt.scatter(features,dependent,color='red')
plt.plot(features_grid,regressor.predict(features_grid),color='blue')
plt.title('Truth or Bluff (SVR Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()