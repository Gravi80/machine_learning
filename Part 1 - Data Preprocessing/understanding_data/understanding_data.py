# Importing the libraries
import numpy as np
import pandas as pd
from pandas import set_option

# Importing the dataset
dataset = pd.read_csv('../dataset/Data.csv') # DataFrame

# Descriptive Statistics
set_option('display.width', 100)
set_option('precision', 3)
dataset.describe()  # lists 8 statistical properties of each attribute.


# Dimensions of Your Data
dataset.shape # You can see that the dataset has 10 rows and 2 columns.

# Data Type For Each Column
dataset.dtypes


# Class Distribution/Classification [ dataset.groupby('column_name') ]
dataset.groupby('Country').size()


# Correlations Between Attributes
	# Correlation refers to the relationship between two variables and how they may or may not change together.
	# The most common method for calculating correlation is Pearson’s Correlation Coefficient, that assumes a normal distribution of the attributes involved. 
	# A correlation of -1 or 1 shows a full negative or positive correlation respectively.

	# Whereas a value of 0 shows no correlation at all.

dataset.corr(method='pearson')
# >>> dataset.corr(method='pearson')
#           Age  Salary
# Age     1.000   0.982
# Salary  0.982   1.000


# Skew of Univariate Distributions
	# Image : univariate_skew_distribution.jpg
	# Skew refers to a distribution that is assumed Gaussian (normal or bell curve) that is shifted or squashed in one direction or another.
	# Knowing that an attribute has a skew may allow you to perform data preparation to correct the skew and later improve the accuracy of your models.
dataset.skew()
# The skew result show a positive (right) or negative (left) skew. Values closer to zero show less skew.


