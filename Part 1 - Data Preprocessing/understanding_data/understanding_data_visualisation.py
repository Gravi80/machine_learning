# Importing the libraries
from matplotlib import pyplot
import pandas as pd
from pandas import set_option
import numpy as np

# Importing the dataset
dataset = pd.read_csv('../dataset/Data.csv') # DataFrame

# Histograms
	# A fast way to get an idea of the distribution of each attribute is to look at histograms.
	# Histograms group data into bins and provide you a count of the number of observations in each bin. 
	# From the shape of the bins you can quickly get a feeling for whether an attribute is Gaussian, skewed or even has an exponential distribution.
dataset.hist()
pyplot.show()
	# Image: histogram_distribution.png
	# We can see that attributes "age", "pedi" and "test" may have an exponential distribution.
	# We can also see that perhaps the "mass" and "pres" and "plas" attributes may have a Gaussian or nearly Gaussian distribution.


# Density Plots		
	# Another way of getting a quick idea of the distribution of each attribute.
dataset.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
pyplot.show()


# Box and Whisker Plots (boxplots for short)
	# Useful for indicating whether a distribution is skewed and whether there are potential unusual observations (outliers) in the data set. 
	# Boxplots summarize the distribution of each attribute, drawing a line for the 
	# median (middle value) and a box around the 25th and 75th percentiles (the middle 50% of the data).

	# The whiskers give an idea of the spread of the data and dots outside of the whiskers show candidate 
	# outlier values (values that are 1.5 times greater than the size of spread of the middle 50% of the data).

dataset.plot(kind='box', subplots=True, layout=(3,3), sharex=False, sharey=False)	
pyplot.show()
	
	# Quartiles
	# A Quartile is a percentile measure that divides the total of 100% into four equal parts: 25%, 50%, 75% and 100%.
	
	#  Q1(quartile 1 ) separates the bottom 25% of the data from the top 75%.
	#  Q2(quartile 2 ) is the mean or average.
	#  Q3(quartile 3 ) separates the top 25% of the data from the bottom 75%.

	# The interquartile range or IQR is the distance between the first and third quartiles. 
	# It is sometimes called the H-spread and is a stable measure of disbursement.  
	# It is obtained by evaluating Q3−Q1 .
	# Image: box_whisker_plots.png

# Skewed data show a lopsided boxplot, where the median cuts the box into two unequal pieces. 
	# If the longer part of the box is to the right (or above) the median, the data is said to be skewed right. 
	# If the longer part is to the left (or below) the median, the data is skewed left.
	# Image : box_plots_skew_curve.png


# In order to be an outlier, the data value must be:
# 1). larger than Q3 by at least 1.5 times the interquartile range (IQR), or
# 2). smaller than Q1 by at least 1.5 times the IQR.

