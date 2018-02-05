# [R&D Spend, Administration, Marketing Spend, State, Profit]
# Multiple Linear Regression

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
np.set_printoptions(threshold=np.nan,formatter={'float': lambda x: "{0:0.0f}".format(x)})

# Importing the dataset
dataset = pd.read_csv('../dataset/50_Startups.csv')
features = dataset.iloc[:, :-1].values  # features.shape  = (50, 4) [ Matrix that has 4 column ]
dependent = dataset.iloc[:, 4].values   # dependent.shape = (50,)	[ No columns, i.e its a vector ]



# Encoding Categorical data

# LabelEncoder	=> Encode categories into numbers [Integer Encoding]
# For categorical variables where no such ordinal relationship exists, 
# the integer encoding is not enough.
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_state = LabelEncoder()
features[:,3] = labelencoder_state.fit_transform(features[:,3])

# OneHotEncoder => Remove any relational order
# A one-hot encoding can be applied to the integer representation.
# This is where the integer encoded variable is removed and a new binary variable is added for each unique integer value.
onehotencoder = OneHotEncoder(categorical_features=[3])
features = onehotencoder.fit_transform(features).toarray() # features.shape  = (50, 6)
# State column is replaced by 3 dummy variables[California, Florida, New York]



# Avoiding the dummy variable trap
features = features[:,1:] # Removed first column(0) from features, [Can be skipped] Python library will take care of it



# Splitting the dataset into Training set and Test set
from sklearn.cross_validation import train_test_split
features_train,features_tests,dependent_train,dependent_tests = train_test_split(features,dependent,test_size=0.2, random_state=0)
	# features_train.shape  => (40, 5)
	# dependent_train.shape => (40,)
	# features_tests.shape  => (10, 5)
	# dependent_tests.shape	=> (10,)


# No need of Feature Scaling, Python ML library will take care of it


# Fitting Multiple Linear Regression to the training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(features_train,dependent_train) # Fit Multiple Linear Regressior to training set


# Predicting the test set results
# Will contain predicted salary for all the observations of our test set
dependent_predictions = regressor.predict(features_tests)
