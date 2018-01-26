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
