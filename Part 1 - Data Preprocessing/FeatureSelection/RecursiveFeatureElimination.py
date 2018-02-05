# The Recursive Feature Elimination (or RFE) works by recursively removing attributes and 
# building a model on those attributes that remain.

# It uses the model accuracy to identify which attributes (and combination of attributes) 
# contribute the most to predicting the target attribute.

# The example below uses RFE with the logistic regression algorithm to select the top 3 features.

# Feature Extraction with RFE
from pandas import read_csv
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression

# load data
filename = '../understanding_data/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

# feature extraction
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)

print("Num Features: %d") % fit.n_features_
	# Num Features: 3
print("Selected Features: %s") % fit.support_
	# Selected Features: [ True False False False False  True  True False]
print("Feature Ranking: %s") % fit.ranking_
	# Feature Ranking: [1 2 3 5 6 1 1 4]

# You can see that RFE chose the top 3 features as preg, mass and pedi.



