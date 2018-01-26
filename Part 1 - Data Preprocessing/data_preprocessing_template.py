# [Country, Age, Salary, Purchased]
# Data Preprocessing Template

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('dataset/Data.csv') # DataFrame
# loc, iloc[rows, columns]
features = dataset.iloc[:, :3].values	# Matrix/Features from Independent variables
dependent_var = dataset.iloc[:, 3].values # Dependent variable



# Taking care of missing data
from sklearn.preprocessing import Imputer
# sklearn => scikit-learn, contains libraries to make machine learning models
# preprocessing => contains lots of classes, methods to pre-process any dataset.
# Imputer => Imputation transformer for completing missing values. This will allow us
# 			 to take care of missing data

# missing values in the dataset variable are represented by NaN
imputer = Imputer(missing_values = 'NaN', strategy= 'mean', axis=0)
# Fit the imputer object to the columns[Age, Salary] containing missing data in features
imputer = imputer.fit(features[:,1:3])

# Replace the missing data of matrix features by the mean of the column
# features[missing dat columns] = imputer.transformer(features[missing dat columns])
features[:,1:3] = imputer.transform(features[:,1:3])



# Encoding Categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
# Fit the labelencoder_country to the country column
labelencoder_country = LabelEncoder()
features[:,0] = labelencoder_country.fit_transform(features[:,0])
# We have replaced text by numbers but ML models are based on Maths equations and equations 
# in the model will take decisions by comparing these non-comparable values
# To prevent this we will use Dummy Variables/Encoding, further README.txt
# OneHotEncoder(column index)
onehotencoder = OneHotEncoder(categorical_features=[0])
features = onehotencoder.fit_transform(features).toarray()

# For Purchased column/variable we don't need to use OneHotEncoder. 
# Since this is a dependent Variable, the ML model will know that its a category and there is no 
# comparable relation between the two
labelencoder_dependent_var = LabelEncoder()
dependent_var = labelencoder_dependent_var.fit_transform(dependent_var)


