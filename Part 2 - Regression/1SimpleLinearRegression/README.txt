The dataset(Salary_Data) contains 2 columns and 30 rows:
YearsExperience,Salary

Find correlation b/w YearsExperience and Salary(i.e Best fitting line for this relationship).


Regression attempts to determine the strength of the relationship between one dependent variable (usually denoted by Y) and a series of other changing variables (known as independent variables).


Simple linear regression is a statistical method that allows us to summarize and study relationships between two continuous (quantitative) variables:

* One variable, denoted x, is regarded as the predictor, explanatory, or independent variable.
* The other variable, denoted y, is regarded as the response, outcome, or dependent variable.

The equation that describes how y is related to x is known as the regression model.
Simple linear regression gets its adjective "simple," because it concerns the study of only one predictor variable. In contrast, multiple linear regression, gets its adjective "multiple," because it concerns the study of two or more predictor variables.

In this simple model, a straight line approximates the relationship between the dependent variable and the independent variable.
https://www.varsitytutors.com/hotmath/hotmath_help/topics/scatter-plots.html

Relationships
-------------
1). Deterministic (or functional) relationships :
	The equation exactly describes the relationship between the two variables.
	Ex- 
		Circumference = π × diameter
		Ohm's Law: I = V/r, where V = voltage applied, r = resistance, and I = current.


2). Statistical relationships :
	Relationship between the variables is not perfect.


Step1
=====
************************************************************
Equations of straight line:
y = mx + c

m => Slope, It is the change in y for a unit change in x along the line.
	 The slope formula is m= y2-y1 over x2-x1.
c => Constant, It is the y intercept, the place where the line crosses the y axis.
	 It is simply the value at which the fitted line crosses the y-axis.
	 http://blog.minitab.com/blog/adventures-in-statistics-2/regression-analysis-how-to-interpret-the-constant-y-intercept

Calculate slope for a set of ordered pairs 
https://www.varsitytutors.com/hotmath/hotmath_help/topics/line-of-best-fit
************************************************************

The equation that describes how y is related to x is known as the regression model.
Equation => Image: equation.png, equation2.png

y  => Dependent Variable (how does salary change with user experience)
X  => Independent Variable
b1 => How a unit change in X1 affects a unit change in y
b0 => Constant, It is the y intercept, what is the salary with 0 Experience.


Step2
=====
Simple linear regression Intuition :

Image: linear_regression_intuition2.png
Red(yi)   => Where the person is sitting in terms of salary
The model line(Black) tells where the person should be according to model.
Green(ŷi) => Where the person should be sitting according to the model.

The simple linear regression draws lots of Black lines, and looks for a line which has minimum sum of squares. This line will be the best fitting line.



