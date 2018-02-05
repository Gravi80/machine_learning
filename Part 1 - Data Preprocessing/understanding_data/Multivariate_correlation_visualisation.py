# Importing the libraries
from matplotlib import pyplot
import pandas as pd
from pandas import set_option
import numpy as np
from pandas.tools.plotting import scatter_matrix

# Importing the dataset
filename = 'pima-indians-diabetes.data.csv'
names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class'] 
dataset = pd.read_csv(filename, names=names)

# Correlation Matrix Plot
	# Correlation gives an indication of how related the changes are between two variables. 
	# If two variables change in the same direction they are positively correlated. 
	# If they change in opposite directions together (one goes up, one goes down), then they are negatively correlated.
correlations = dataset.corr()

# plot correlation matrix
fig = pyplot.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(correlations, vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,9,1)
ax.set_xticks(ticks)
ax.set_yticks(ticks)
ax.set_xticklabels(names)
ax.set_yticklabels(names)
pyplot.show()
# Image : Correlation_Matrix_Plot.png	
	# We can see that the matrix is symmetrical, 
	# i.e. the bottom left of the matrix is the same as the top right.
	# Each variable is perfectly positively correlated with each other (as you would have expected) in the diagonal line from top left to bottom right.



# Scatter Plot Matrix
	# A scatter plot shows the relationship between two variables as dots in two dimensions, one axis for each attribute.
		# You can create a scatter plot for each pair of attributes in your data. Drawing all these scatter plots together is called a scatter plot matrix.
scatter_matrix(dataset)
pyplot.show()
# There is little point of drawing a scatter plot of each variable with itself, the diagonal shows histograms of each attribute.
# Image: Scatter_Plot_Matrix.png

