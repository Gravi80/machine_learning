The dataset(50_Startups) contains 5 columns and 50 rows:
R&D Spend,Administration,Marketing Spend,State,Profit

For a state how much a company spent on R&D, Administration and Marketing in a financial year.
And Profit generated for that financial year.

Dependent Variable 		=> Profit
InDependent Variables 	=> R&D Spend,Administration,Marketing Spend,State

Predict profit based on R&D Spend,Administration,Marketing Spend and State.
i.e which of the spend brings better result of profit in a state OR is there any correlation between R&D,Administration,Marketing Spend and in which state the company operate with Profit.



Multiple linear regression, gets its adjective "multiple," because it concerns the study of two or more predictor variables.

Image => multiple_linear_regression.png


Dummy Variable
==============
Image : dummy_variable.png

State[Categorical Variable] is a string and can't be added to the equation.
When you have Categorical Variable in your regression model, you need to create dummy variable.

1). Find All different categories.
2). For every category create a new column
	Image : dummy_variable2.png
3). To populate the New York column, find all the rows where state is NewYork and Put 1.
	And similar for column California do the same thing.
	Image : dummy_variable3.png
4). Instead of State use the New York column. D1 is the dummy variable for NewYork.
	We can skip California column bcz all our data is preserved in New York column itself.
	If D1 = 1 , comany operates in New York otherwise in California.
	Image : dummy_variable4.png

	Dummy Variable Trap
	===================
	It's always a bad idea to include all dummy variables in model equation.Always omit 1 dummy variable.

	Image : dummy_variable5.png

	The Dummy Variable trap is a scenario in which the independent variables are multicollinear - a scenario in which two or more variables are highly correlated; in simple terms one variable can be predicted from the others.

	https://www.youtube.com/watch?v=qrWx3OjZL3o


Constructing Multiple Linear Regression Model
=============================================
We need to decide which Independent variable to keep and which one to throw out.
Why not everything:
1). If you through lots of variable/stuffs to your model then your model will not be good model i.e 	won't be relaible [Garbage Model]
2).	Explaing/Understanding your model will be difficult.So, you should keep only very important			variables that actually predict something.

5 methods of building a model :
	Step-by-step-Blueprints-For-Building-Models.pdf
	Bidirectional Elimination is the more general approach.

	Backward Elimination
	====================
	The variable that is least significant--that is, the one with the largest P value--is removed and the model is refitted. Each subsequent step removes the least significant variable in the model until all remaining variables have individual P values smaller than some value, such as 0.05 or 0.10.

	AIC does correspond to using a p-value of 0.15 (or to be more precise, 0.1573)

	







