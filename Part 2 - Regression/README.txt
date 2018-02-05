Regression models (both linear and non-linear) are used for predicting a real value, like salary for example.

Assumptions of a Linear Regression model :
1). Linear relationship (Co-variance)
		Linear regression needs the relationship between the independent and dependent variables to be linear. When one goes up other also goes up and when one goes down other also goes down.
		It is also important to check for outliers since linear regression is sensitive to outlier effects.
		If the scatter plot follows a linear pattern (i.e. not a curvilinear pattern) that shows that linearity assumption is met.  

		Image => linear-nonlinear-relationships.png, non_linear_relationships.png

		If the relationship displayed in your scatterplot is not linear, you will have to either run a non-linear regression analysis, perform a polynomial regression or "transform" your data.


2). Homoscedasticity(meaning "same variance" or "having the same scatter")
	The variances along the line of best fit remain similar as you move along the line.
	Homoscedasticity describes a situation in which the error term (that is, the “noise” or random disturbance in the relationship between the independent variables and the dependent variable) is the same across all values of the independent variables.

	Image => homoscedasticity.png, homoscedasticity2.png


3). Multivariate normality
	Linear regression analysis requires all variables to be multivariate normal. This assumption can best be checked with a histogram or a Q-Q-Plot.

	A multivariate regression is a technique that estimates a single regression model with more than one outcome variable. 


4). Independence of errors


5). No or little multicollinearity
	Multicollinearity occurs when the independent variables are too highly correlated with each other.



Residuals
=========
The difference between the observed value of the dependent variable (y) and the predicted value (ŷ) is called the residual (e). Each data point has one residual.
				Residual = Observed value - Predicted value 
					e = y - ŷ
Both the sum and the mean of the residuals are equal to zero. That is, Σ e = 0 and e = 0.
http://stattrek.com/regression/residual-analysis.aspx					




best linear unbiased estimator(BLUE)
