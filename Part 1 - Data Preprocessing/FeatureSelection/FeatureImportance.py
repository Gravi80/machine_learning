# Bagged decision trees like Random Forest and Extra Trees can be used to estimate the 
# importance of features.

# Feature Importance with Extra Trees Classifier
from pandas import read_csv
from sklearn.ensemble import ExtraTreesClassifier
# load data
filename = '../understanding_data/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
model = ExtraTreesClassifier()
model.fit(X, Y)
print(model.feature_importances_)
	# [0.115 0.227 0.102 0.07  0.08  0.138 0.118 0.148]
# You can see that we are given an importance score for each attribute where the larger the score, the more important the attribute. 
# The scores suggest at the importance of plas, age and mass.