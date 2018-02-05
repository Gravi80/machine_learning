# Features that have the strongest relationship with the output variable.
# The scikit-learn library provides the SelectKBest class that can be used with a suite of different statistical tests to select a specific number of features.

# chi-squared (chi2) statistical test to select 4 of the best features from the Pima Indians onset of diabetes dataset.
from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import chi2
# load data
filename = '../understanding_data/pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(filename, names=names)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
# feature extraction
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)
# summarize scores
set_printoptions(precision=3)
print(fit.scores_)
	# [ 111.52  1411.887   17.605   53.108 2175.565  127.669    5.393  181.304]
	# You can see the scores for each attribute and the 4 attributes chosen 
	# (those with the highest scores): plas, test, mass and age.
features = fit.transform(X)

# summarize selected features values
print(features[0:5,:])
	# [[148.    0.   33.6  50. ]
	#  [ 85.    0.   26.6  31. ]
	#  [183.    0.   23.3  32. ]
	#  [ 89.   94.   28.1  21. ]
	#  [137.  168.   43.1  33. ]]



