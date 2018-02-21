# Decision tree Regression [A non-continuous model]

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
	# Getting all your data on the same scale. 
	# The main advantage of scaling is to avoid attributes in greater numeric ranges dominating those in smaller numeric ranges.

# Fitting Decision Tree Regression model to the dataset
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(features,dependent)

# Predicting a new result with Decision Tree Regression model
y_pred = regressor.predict(6.5)
	# array([150000.])

# Visualising Decision Tree Regression model results
plt.scatter(features,dependent,color='red')
plt.plot(features,regressor.predict(features),color='blue')
plt.title('Truth or Bluff (Decision Tree Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# Visualising Decision Tree Decision Tree Regression model results (for higher resolution and smoother curve)
features_grid = np.arange(min(features),max(features),0.01) # will contains all the levels from 1 to 10, along with imaginary level 1.1, 1.2 ..... 9.9
features_grid = features_grid.reshape((len(features_grid),1))    # convert feature grid to matrix  reshape(rows,column)
plt.scatter(features,dependent,color='red')
plt.plot(features_grid,regressor.predict(features_grid),color='blue')
plt.title('Truth or Bluff ( Smooth Decision Regression Model)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# The regression model is considering avg value between the time-interval for prediction