#[Position,Level,Salary] , Salaries at 10 different positions
# Bluffing detector

# Ploynomial Regression
 # Importing the libraries
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
np.set_printoptions(threshold=np.nan,formatter={'float': lambda x: "{0:0.0f}".format(x)})

# Importing the dataset
dataset = pd.read_csv('../dataset/Position_Salaries.csv')
dataset.iloc[:,1:3].plot(kind='scatter',x="Level",y="Salary")
# df.plot(style=".")
plt.show()

# Position column is already encoded in Level column
features = dataset.iloc[:, 1].values  # features.shape  = (10,) [ No columns, i.e its a vector ]
# We want features to be always considered as Matrix
features = dataset.iloc[:, 1:2].values  # features.shape  = (10,1) [ No columns, i.e its a vector ]
dependent = dataset.iloc[:, 2].values   # dependent.shape = (10,)	[ No columns, i.e its a vector ]

# Since dataset is small we can skip Splitting


# Compare below regression models
# 1). Fitting Linear Regression to the dataset
from sklearn.linear_model import LinearRegression
lin_reg = LinearRegression()
lin_reg.fit(features,dependent)

# 2). Fitting Polynomial Regression to the dataset
from sklearn.preprocessing import PolynomialFeatures

# PolynomialFeatures will transform our Matrix(features) into features,features^2,features^3...features^n. 
# These will be new Independent variables
poly_reg = PolynomialFeatures(degree=2)
features_poly = poly_reg.fit_transform(features) # features_poly.shape = (10, 3) ,  [Constant b0, Level, Level^2]
# poly_reg.fit(features_poly)
# Include features_poly into Multiple Linear regression model
lin_reg2 = LinearRegression()
lin_reg2.fit(features_poly,dependent)

# Visualising the Linear Regression results
plt.scatter(features,dependent,color='red')
plt.plot(features,lin_reg.predict(features),color='blue')
plt.title('Truth or Bluff (Linear Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()
# Visualising the Polynomial Regression results
plt.scatter(features,dependent,color='red')
plt.plot(features,lin_reg2.predict(poly_reg.fit_transform(features)),color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()


# With degree 3
poly_reg = PolynomialFeatures(degree=3)
features_poly = poly_reg.fit_transform(features) # features_poly.shape = (10, 3) ,  [Constant b0, Level, Level^2]
lin_reg2 = LinearRegression()
lin_reg2.fit(features_poly,dependent)

# Visualising the Polynomial Regression results
plt.scatter(features,dependent,color='red')
plt.plot(features,lin_reg2.predict(poly_reg.fit_transform(features)),color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()

# With degree 4
poly_reg = PolynomialFeatures(degree=4)
features_poly = poly_reg.fit_transform(features) # features_poly.shape = (10, 3) ,  [Constant b0, Level, Level^2]
lin_reg2 = LinearRegression()
lin_reg2.fit(features_poly,dependent)

# Visualising the Polynomial Regression results
plt.scatter(features,dependent,color='red')
plt.plot(features,lin_reg2.predict(poly_reg.fit_transform(features)),color='blue')
plt.title('Truth or Bluff (Polynomial Regression)')
plt.xlabel('Position level')
plt.ylabel('Salary')
plt.show()



# Predicting a new result with Linear Regression
lin_reg.predict(6.5) # Employee having level/experience of 6.5 years
    # array([330379])

# Predicting a new result with Polynomial Regression
lin_reg2.predict(poly_reg.fit_transform(6.5))
    # array([158862])