# Random Forest Regression [non-continuous model]

# Importing the libraries
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
np.set_printoptions(threshold=np.nan,formatter={'float': lambda x: "{0:0.0f}".format(x)})

# Importing the dataset
dataset = pd.read_csv('../dataset/Position_Salaries.csv')

# Derive features and dependent variables. Features should always be considered as Matrix
features = dataset.iloc[:, 1:2].values  # features.shape  = (10,1) [ No columns, i.e its a vector ]
dependent = dataset.iloc[:, 2].values   # dependent.shape = (10,)	[ No columns, i.e its a vector ]

# Encoding Categorical data

# Splitting the dataset into Training set and Test set

# Feature Scaling [ Handled by most of the ML algorithms ]
	# A case of getting all your data on the same scale. 
	# The main advantage of scaling is to avoid attributes in greater numeric ranges dominating those in smaller numeric ranges.

# Fitting Random Forest model to the dataset
from sklearn.ensemble import RandomForestRegressor
n_estimators = 10 #number of trees
regressor = RandomForestRegressor(n_estimators=n_estimators,random_state=0)
regressor.fit(features,dependent)

# Predicting a new result with  Random Forest Regression model
y_pred = regressor.predict(6.5)
	# array([167000])

# Visualising  Random Forest Regression model results (for higher resolution and smoother curve)
features_grid = np.arange(min(features),max(features),0.01) # will contains all the levels from 1 to 10, along with imaginary level 1.01, 1.02 ..... 9.99
features_grid = features_grid.reshape((len(features_grid),1))    # convert feature grid to matrix  reshape(rows,column)
plt.scatter(features,dependent,color='red')
plt.plot(features_grid,regressor.predict(features_grid),color='blue')
plt.title('Truth or Bluff ( Random Forest Regression Model, n_estimators={0})'.format(n_estimators))
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


from sklearn.ensemble import RandomForestRegressor
n_estimators = 100 #number of trees
regressor = RandomForestRegressor(n_estimators=n_estimators,random_state=0)
regressor.fit(features,dependent)
y_pred = regressor.predict(6.5)
	# array([158300])


from sklearn.ensemble import RandomForestRegressor
n_estimators = 300 #number of trees
regressor = RandomForestRegressor(n_estimators=n_estimators,random_state=0)
regressor.fit(features,dependent)
y_pred = regressor.predict(6.5)
	# array([160333])
