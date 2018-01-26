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



