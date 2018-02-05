Based on Duper Datascience tutorials
Datasets = https://www.superdatascience.com/machine-learning/


Printing numpy float list/array:
import numpy as np
np.set_printoptions(threshold=np.nan,formatter={'float': lambda x: "{0:0.0f}".format(x)})
