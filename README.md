Based on Duper Datascience tutorials
Datasets = https://www.superdatascience.com/machine-learning/


Classification : Discrete data [Counted] [ Discrete data contains finite values that have nothing in-between, Days of the week]
                 The term discrete implies distinct or separate. It includes only those values that can only be counted in whole numbers or integers and are separate which means the data cannot be broken down into fraction or decimal.

                 Discrete Data can only take certain values.
                 Example: the number of students in a class (you can't have half a student).
                
Regression : Continuous data [  Measured ]
              It can take any numeric value, within a finite or infinite range of possible value.
              
              Continuous data are not restricted to defined separate values, but can occupy any value over a continuous range. Between any two continuous data values there may be an infinite number of others. Continuous data are always essentially numeric.


Printing numpy float list/array:

import numpy as np

np.set_printoptions(threshold=np.nan,formatter={'float': lambda x: "{0:0.0f}".format(x)})

Setup
--
    python3 -m venv machine_learn
    source machine_learn/bin/activate
    pip install -r requirement.txt

    python other_examples/line_equation.py