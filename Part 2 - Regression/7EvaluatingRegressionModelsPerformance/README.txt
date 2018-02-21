Simple Linear regression Intuition :
===============================
Image: linear_regression_intuition.png

Red(yi)   => Where the person is sitting in terms of salary
The model line(Black) tells where the person should be according to model.
Green(ŷi) => Where the person should be sitting according to the model.

The simple linear regression draws lots of Black lines, and looks for a line which has minimum sum of squares. This line will be the best fitting line.



R Squared [Goodness of Fit]
===========================

Instead of drawing regression line, lets draw the avg. line [avg. salary across all observations]

Image: avg_line_SSres.png
SSres = Sum of squares of residual [against the fitting line]
SStot = Total sum of squares 	   [against the avg. line]

To get the best fitting line we need to minimise the SSres as much as possible because this will give us minimum [SSres/SStot] value.


R Square tells how good is your line compared to the avg. line(which any one can think of).

Best R Square = 1
Worst R Square = 0 or Negative[Your predictions/fitting_line is worse than the avg. line]


Same method will be used for Multiple linear regression models.


With R Square the problems occurs if we start adding new variables[impacting the dependent variable] to the model.

Image : Adding_3rd_variable.png

After adding the Third variable and running our model we need to check did R Square became better.

Image: R_Square_problem.png
The problem is R Square will never decrease. 

Either the new variable will help in minimising SSres [The regression model somehow will find a way to give a coefficient to the variable that will help minimise the SSres]
In that case [SSres/SStot] will decrease So, R Square will increase.


If the new variable[like: last digit of mobile_number] doesn't have any correlation with the Dependent variable. There is no causal relationship bcz last digit of mobile_number will not have any impact of the salary.
But since we have added the variable so there will be a random slight relation between Dependent variable and new variable. So, R Square will increase OR decrease by that tiny little bit.

------------------------------
Either R Square will increase or won't change at all(might have slight change). So, you can add variables but you won't know if those variables are helping your model or not.
------------------------------


Adjusted R Squared
==================
Adjusted R Squared solve the above problem.
It has a penalisation factor. It penalises you for adding variables that don't help your model.

Image: adjusted_R_2.png

p => Number of Independent Variables
	 P increase when you increase number of Independent Variables. With this the denominator decreases and the Ratio increases.

	 As the Ratio increases the below image bit increases aswell:
	 	Image: Adjusted_R_square_ratio.png
	 And (1 - above_bit) decreases

	 As you adding more Regressors / Independent_Variables, the adjusted R Square is decreasing.

	
	 Also when R Square increases the below image bit decreases:
	 	Image : R_square_decrease.png
	 That means the whole part on Right hand side increases.

	 So, there is a fair battle between R Square and Number of Independent variables.
	 If your variable is not helping the model then R_square will have insignificant increase and the penalisation factor will drive Adjusted R Squared down.
	 If your variable is helping the model a lot then the increase in R_square will be substantial and it will overwhelm the penalisation factor and will drive Adjusted R Squared Up.
